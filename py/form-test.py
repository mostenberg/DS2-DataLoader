#!/usr/bin/python3

print('Content-Type: text/html; charset=utf-8\n')

import os
requestMethod = os.environ['REQUEST_METHOD']
tblrqs = {}
if requestMethod == 'GET':
  queryParamsList = os.environ['QUERY_STRING'].split('&')
  for queryParam in queryParamsList:
    keyAndParam = queryParam.split('=')
    tblrqs[keyAndParam[0]] = keyAndParam[1]
  print('GET request data was: ' + str(tblrqs))
elif requestMethod == 'POST':
  import cgi
  queryParamsList = cgi.FieldStorage()
  for wrkkey in queryParamsList:
    if isinstance(queryParamsList[wrkkey], list):
      wrkvlx = queryParamsList[wrkkey][0].value
    else:
      wrkvlx = queryParamsList[wrkkey].value
    tblrqs[wrkkey] = wrkvlx
  print('POST request data: ' + str(tblrqs))
else:
  print('Request method \'' + requestMethod + '\' not supported yet')

