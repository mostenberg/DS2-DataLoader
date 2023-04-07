#!/usr/bin/env bash
#This is the stack script which will be used to generate a sample webserver. The webserver can push data into an Elastic server to simulate DataStream2 activatiion
#<UDF name="CERT_EMAIL" label="The email address to use for your certificate" default="youremailaddress@goes.here">
## Enable logging
set -o pipefail
exec > >(tee /dev/ttyS0 /var/log/stackscript.log) 2>&1
## Update packages
sudo apt update -y
sudo apt upgrade -y
## Install apache2 (could take 1 minute)
sudo apt install apache2 -y
## Create a directory for the virtual host
sudo mkdir -p /var/lamp2/linode-demo
## Change owner of the virtual directory to user
sudo chown -R $USER:$USER /var/lamp2/linode-demo
## Install firewall and open ports for https
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw allow https
sudo ufw allow http
sudo ufw -force enable
sudo ufw status
##Install certbot, which relies on snapd package manager
sudo apt install snapd -y
sudo snap install core
sudo snap refresh core
#Install certbot by using snap
#First, remove old certbot
sudo apt remove certbot
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
## Store IPV4 address in an env variable MYIP
export MYIP=$(hostname -I | awk '{print $1}')

#Some functions to lookup reverse DNS
function system_primary_ip {
    local ip_address="$(ip a | awk '/inet / {print $2}')"
    echo $ip_address | cut -d' ' -f 2 | cut -d/ -f 1
}
function system_primary_ipv6 {
    ip -6 a | grep inet6 | awk '/global/{print $2}' | cut -d/ -f1
}
function system_private_ip {
    local ip_address="$(ip a | awk '/inet 192.168/ {print $2}')"
    echo $ip_address | cut -d ' ' -f 2 | cut -d/ -f 1
}
function get_rdns {
    # $1 - The IP address to query
    [ ! -e /usr/bin/host ] && system_install_package dnsutils
    host "$1" | awk '/pointer/ {print $5}' | sed 's/\.$//'
}
function get_rdns_primary_ip {
    # returns the reverse dns of the primary IP assigned to this system
    get_rdns $(system_primary_ip)
}
##Get and install certificate
sudo certbot --apache --email=$CERT_EMAIL --non-interactive --agree-tos --domain=$(get_rdns_primary_ip)
## In Apache, enable the cgi module to allow python processing
sudo a2enmod cgid
## Restart Apache2
sudo systemctl restart apache2
## Modify the apache config files to allow python files to execute as cgi scripts
sed -i 's|ScriptAlias /cgi-bin/ .*|ScriptAlias /py/ /var/www/py/| ; s|OwnerMatch|OwnerMatch\n\t\t\tAddHandler cgi-script .cgi .py| ; s|<Directory "/usr/lib/cgi-bin">|<Directory "/var/www/py">|' /etc/apache2/conf-available/serve-cgi-bin.conf
sudo mkdir /var/www/py
#Add the data loader python code which will generate dummy data and send to the elastic server
cd /var/www/py
wget https://raw.githubusercontent.com/mostenberg/DS2-DataLoader/master/py/sendBulkDSData.py
sudo chmod +x /var/www/py/sendBulkDSData.py
#Download the data template which lists fields and values to be used (list of values for each field) to randomly generate data to push into elastic
wget https://raw.githubusercontent.com/mostenberg/DS2-DataLoader/master/py/singleRequestWithListFields.json
wget https://raw.githubusercontent.com/mostenberg/DS2-DataLoader/master/py/singleBigFilesRequestWithListFields.json
wget https://raw.githubusercontent.com/mostenberg/DS2-DataLoader/master/py/sampleErrorDataWithListFields.json
#Create a text file which will hold the bulk data for sending to Elastic
echo "dummy data will be overwritten at first run" > /var/www/py/bulkFile.txt
#Make apache the owner of the file so it can write the bulk send data to the file from the python scripts
chgrp www-data /var/www/py/bulkFile.txt 
chmod g+w /var/www/py/bulkFile.txt
#Download the data loader web page from github
cd /var/www/html
wget https://raw.githubusercontent.com/mostenberg/DS2-DataLoader/master/html/ds2.html
#Wait 10 sec then restart Apache2
sleep 10
sudo systemctl restart apache2
echo "Instance setup is complete. Please go to browser to pull up webpage or go to <yourdomain>/ds2.html to pull up data loader page."
