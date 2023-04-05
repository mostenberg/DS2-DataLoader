# DataStream-DataLoader2

## Background

This repository contains assets related to the Linode / Elastic workshop.
The workshop is designed to show how DataStream2 data can be viewed in Elastic using Linode servers. There are a few components to this repository:

- ds2.html: A web page where you can enter the url, username of your elastic server
- sendBulkDSData.py : Python code which will take the URL and login information of your elastic server and send simulated data to that server
- singleRequestWithListFields.json : A template for the data which will be sent to the elastic server. It includes various fields with a list of values. The values will be randomized and sent to the Elastic server to simulate DS2 usage.
- DataLoaderStackScript.bash : This is the stack script which will be run to generate the server (kept in github since Linode stack scripts doesn't have version control)
