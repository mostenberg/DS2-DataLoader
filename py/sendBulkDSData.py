#!/usr/bin/python3

import requests
import json
import time
import random
import os
import urllib
import logging
from urllib.parse import urlparse

# Trying for bulk request


def sendDataToElastic(url, username, password, count, jsonData):
    headers = {"Content-type": "application/json"}
    auth = (username, password)
    # This is where we store the large file we're creating
    bulkFile = open("bulkFile.txt", "w")

    print(f"Count is: {count}")
    for x in range(int(count)):
        # print(f"x is {x}")
        jsonObj = json.loads(jsonData)  # Turns file json into object
        # timestamp from now back 1 day
        jsonObj["reqTimeSec"] = int(time.time()-random.randrange(1, 60*60*24))

        for key in jsonObj:  # Loop through all elements of send data
            # If list of values is provided, randomly pick one
            if type(jsonObj[key]) == list:
                jsonObj[key] = jsonObj[key][random.randint(
                    0, len(jsonObj[key])-1)]
        bulkFile.write("{ \"create\" : { \"_index\" : \"datastream2\"} }\n")
        bulkFile.write(json.dumps(jsonObj)+"\n")

    bulkFile.close()

    # Trying for bulk request
    f = open("bulkFile.txt", "r")

    # Send the data to Elastic and get response:
    sendBody = f.read(-1)
    r = requests.post(url, data=sendBody, headers=headers, auth=auth)
    return r.text

# username = "ds2user"
# password = "dddddddddd"
# url = "http://45-79-199-214.ip.linodeusercontent.com:9200/datastream2/_bulk" # This the URL of the Elastic Server
# count = 10000


os.environ['QUERY_STRING']
queryString = os.environ['QUERY_STRING']
params = urllib.parse.parse_qsl(queryString)

print('Content-Type: text/html; charset=utf-8\n')

paramDict = {}
for param in params:
    # print("name:"+param[0]+" value:"+param[1])
    paramDict[param[0]] = param[1]

elasticurl = "http://"+paramDict["elastichostname"]+":9200/datastream2/_bulk"
logging.info('elasticurl is: '+elasticurl)
print('elasticurl is: '+elasticurl)

username = paramDict["username"]
password = paramDict["password"]
numRecords = paramDict["numrecords"]

f = open("singleRequestWithListFields.json", "r")  # Read the doc from a file
myJsonData = f.read(-1)  # Read the entire file into sendBody variable
myJsonData = myJsonData.replace("\n", "")  # Strip any newlines
print("\n******** JSON Data:\n")
print(myJsonData)
print("\n********\n")

myResponse = sendDataToElastic(
    elasticurl, username, password, numRecords, myJsonData)
print("\n****RESPONSE: \n")
print(myResponse)
f.close

# Read the doc from a file
f = open("singleBigFilesRequestWithListFields.json", "r")
myJsonData = f.read(-1)  # Read the entire file into sendBody variable
myJsonData = myJsonData.replace("\n", "")  # Strip any newlines
print("\n***JSON DATA2\n")
print(myJsonData)
print("\n***RESPONSE 2\n")

myResponse = sendDataToElastic(
    elasticurl, username, password, numRecords, myJsonData)
print(myResponse)
print("\n********\n")

f = open("sampleErrorDataWithListFields.json", "r")  # Read the doc from a file
myJsonData = f.read(-1)  # Read the entire file into sendBody variable
myJsonData = myJsonData.replace("\n", "")  # Strip any newlines
print("\n***JSON DATA2\n")
print(myJsonData)
print("\n***RESPONSE 2\n")

myResponse = sendDataToElastic(
    elasticurl, username, password, numRecords, myJsonData)
print(myResponse)
print("\n********\n")
f.close
