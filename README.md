# DataStream-DataLoader2

## Background

This repository contains assets related to the Linode / Elastic workshop.
The workshop is designed to show how DataStream2 data can be viewed in Elastic using Linode servers.

The workshop was broken into 4 sections:

- **Section 1**: Setup a Lamp Server using Linode UI and stack scripts. [details](./instructions/section1.md)
- **Section 2**: Setup an ELK server and load data [details](./instructions/section2.md)
- **Section 3**: Use the Linode User Interface to [details](./instructions/section3.md)
- **Section 4**: Install and setup the Linode command line interface [details](./instructions/section4.md)

Additional reference resources:

- **Sample Elasticsearch queries** : Samples of queries you can use in the 'discover' section on an Elasticsearch server [here](./instructions/SampleElasticSearchQueries.md)
- **Video on Setting up DataStream2** : YouTube video showing how you can setup datastream2 to send information to an ELK server (10 min) [here](https://www.youtube.com/watch?v=v2rZtSSjUDE)

Background assets used to create the website and load data into Elastic server were:

- **ds2.html**: A web page where you can enter the url, username of your elastic server
- **sendBulkDSData.py** : Python code which will take the URL and login information of your elastic server and send simulated data to that server
- **singleRequestWithListFields.json** : A template for the data which will be sent to the elastic server. It includes various fields with a list of values. The values will be randomized and sent to the Elastic server to simulate DS2 usage.
- **DataLoaderStackScript.bash** : This is the stack script which was run to generate the server lamp server (kept in github since Linode stack scripts doesn't have version control)
