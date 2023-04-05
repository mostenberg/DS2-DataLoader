import requests

#url = "http://45-79-199-214.ip.linodeusercontent.com:9200/datastream2/_bulk" # This the URL of the Elastic Server
#url = "http://45-79-199-214.ip.linodeusercontent.com:9200/datastream2/_bulk" # This the URL of the Elastic Server
username = "ds2user"
password = "u34aB6RsO4I4%Uc2qYNGnVS4vlKpvA"

#headers = {"Content-type":"application/json"}
headers = {"Content-type":"application/json"}
auth=(username,password)

#f = open("singleBulkRequest.json","r")

#Works for single request
#url = "http://45-79-199-214.ip.linodeusercontent.com:9200/datastream2/_doc" # This the URL of the Elastic Server
#f = open("singleRequest.json","r")

#Trying for bulk request
url = "http://45-79-199-214.ip.linodeusercontent.com:9200/datastream2/_bulk" # This the URL of the Elastic Server
f = open("singleBulkRequest.json","r")

#Send it and get response:
sendBody = f.read(-1)
print (sendBody)
r=requests.post(url,data=sendBody, headers=headers,auth=auth)
print(r.text)

