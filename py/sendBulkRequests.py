import requests, json, time, random

#Trying for bulk request
def sendDataToElastic(url,username,password,count,jsonData):
    headers = {"Content-type":"application/json"}
    auth=(username,password)
    bulkFile = open("bulkFile.txt","w") # This is where we store the large file we're creating

    print(f"Count is: {count}")
    for x in range(count): 
        #print(f"x is {x}")
        jsonObj=json.loads(jsonData) #Turns file json into object
        jsonObj["reqTimeSec"]=time.time()-random.randrange(1,60*60*24) #timestamp from now back 1 day
        
        for key in jsonObj: #Loop through all elements of send data
            if type(jsonObj[key])==list: #If list of values is provided, randomly pick one
                jsonObj[key]=jsonObj[key][random.randint(0,len(jsonObj[key])-1)] 
        bulkFile.write("{ \"create\" : { \"_index\" : \"datastream2\"} }\n")
        bulkFile.write(json.dumps(jsonObj)+"\n")
    
    bulkFile.close()

    #Trying for bulk request
    f = open("bulkFile.txt","r")

    #Send the data to Elastic and get response:
    sendBody = f.read(-1)
    r=requests.post(url,data=sendBody, headers=headers,auth=auth)
    return r.text


username = "ds2user"
password = "u34aB6RsO4I4%Uc2qYNGnVS4vlKpvA"
url = "http://45-79-199-214.ip.linodeusercontent.com:9200/datastream2/_bulk" # This the URL of the Elastic Server
count = 10000

import os
rqsmtd = os.environ['REQUEST_METHOD']
tblrqs = {}
if rqsmtd == 'GET':
  wrktbl = os.environ['QUERY_STRING'].split('&')
  for wrkarg in wrktbl:
    wrklst = wrkarg.split('=')
    tblrqs[wrklst[0]] = wrklst[1]
  print('GET request data: ' + str(tblrqs))
elif rqsmtd == 'POST':
  import cgi
  wrktbl = cgi.FieldStorage()
  for wrkkey in wrktbl:
    if isinstance(wrktbl[wrkkey], list):
      wrkvlx = wrktbl[wrkkey][0].value
    else:
      wrkvlx = wrktbl[wrkkey].value
    tblrqs[wrkkey] = wrkvlx
    
  print('Print Python response: POST request data: ' + str(tblrqs))
else:
  print('Request method \'' + rqsmtd + '\' not supported yet')


f = open("singleRequestWithListFields.json","r") # Read the doc from a file
myJsonData = f.read(-1) #Read the entire file into sendBody variable
myJsonData=myJsonData.replace("\n","") #Strip any newlines
print (myJsonData)
myResponse=sendDataToElastic(url,username,password,1000,myJsonData)
print (myResponse)
f.close

f = open("singleRequestWithListFields.json","r") # Read the doc from a file
myJsonData = f.read(-1) #Read the entire file into sendBody variable
myJsonData=myJsonData.replace("\n","") #Strip any newlines
print (myJsonData)
myResponse=sendDataToElastic(url,username,password,1000,myJsonData)
print (myResponse)
f.close



