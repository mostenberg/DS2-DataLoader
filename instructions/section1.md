# Section 1: Setup a Lamp server

### Purpose

Become familiar with the Akamai Control Center (Linode) user interface by deploying a website using a 'stack script' in Linode.

## Steps

1. Login to Linode at ‘https://cloud.linode.com and click on ‘Create Linode’
2. In ‘community stack scripts’ click radio button for stack script named: ‘mostenbe/lamp-datastream-loader’
3. Scroll down to form fields and enter:
   - Your email address (for certificate)
   - Images: Ubuntu 22.10 LTS
   - Region: Atlanta
   - Size: Shared CPU - Nanode 1GB
   - Label : lamp-\<yourname>-\<mm-dd-yy>
   - Root Password: \<pick one and make sure to remember it>
4. Scroll to bottom and click ‘Create Linode’
5. Deployment takes about 8 minutes. Use LISH console to watch progress.
6. In Linode console, click on your instance and go to 'network' tab. Locate the rdns which you can use as hostname.
7. Open browser and put in hostname and you should see Apache Ubuntu Default page
8. SUCCESS!! SECTION 1 COMPLETE
