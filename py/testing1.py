#!/usr/bin/python3

import  json, time, random,os,urllib
from urllib.parse import urlparse

queryString="name=Mike&age=34&height=43"
params=urlparse(queryString)
print(params.__dir__());

params2=urllib.parse.parse_qsl(queryString);

paramDict={}
for param in params2:
    print("name:"+param[0]+" value:"+param[1]);
    paramDict[param[0]]=param[1];

print("name is:"+paramDict["name"]);