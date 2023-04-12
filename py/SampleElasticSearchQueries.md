# Elastic Search Sample DataStream2 Queries

## Overview

DataStream2 is Akamai's Edge Server Data Streaming product. It will send JSON data to analysis endpoints such as Elastic Search. DataStream2 has a variety of available fields which may be sent. Full list of fields is [here](https://techdocs.akamai.com/datastream2/v2/reference/data-set-fields-1).

[Elasticsearch](https://www.elastic.co/elasticsearch/) is a RESTful search and analytics engine which allows you to query and report on your data. It uses it's own query syntax to allow you to capture and analyze data.

This document contains some sample queries which will help illustrate how to use Elasticsearch queries to capture information from DataStream2 data

## Sample DataStream Data

For each request sent to an Akamai Edge server, Datastream2 will send back an object in compressed or JSON format with data about the request. A sample request in JSON format is here:

```
{
  "doc": {
    "version": 1,
    "streamId": "12345",
    "cp": "123456",
    "reqId": "1239f220",
    "reqTimeSec": "1678859500.171",
    "bytes": "4995",
    "cliIP": "128.147.28.68",
    "statusCode": "206",
    "proto": "HTTPS",
    "reqHost": "test.hostname.net",
    "reqMethod": "GET",
    "reqPath": "/path1/path2/file.ext",
    "reqPort": "443",
    "rspContentLen": "5000",
    "rspContentType": "text/html",
    "UA": "Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_14_3%29",
    "tlsOverheadTimeMSec": "0",
    "tlsVersion": "TLSv1",
    "objSize": "484",
    "uncompressedSize": "484",
    "overheadBytes": "232",
    "totalBytes": "0",
    "queryStr": "param=value",
    "accLang": "en-US",
    "cookie": "cookie-content",
    "range": "37334-42356",
    "referer": "https%3A%2F%2Ftest.referrer.net%2Fen-US%2Fdocs%2FWeb%2Ftest",
    "xForwardedFor": "8.47.28.38",
    "maxAgeSec": "3600",
    "reqEndTimeMSec": "3",
    "errorCode": "ERR_ACCESS_DENIED|fwd_acl",
    "turnAroundTimeMSec": "11",
    "transferTimeMSec": "125",
    "dnsLookupTimeMSec": "50",
    "lastByte": "1",
    "cacheStatus": "1",
    "cacheable": "1",
    "edgeIP": "23.50.51.173",
    "country": "US",
    "state": "Virginia",
    "city": "HERNDON",
    "serverCountry": "SG",
    "billingRegion": "8",
    "securityRules": "ULnR_28976|3900000:3900001:3900005:3900006:BOT-ANOMALY-HEADER|",
    "ewUsageInfo": "//4380/4.0/1/-/0/4/#1,2\\//4380/4.0/4/-/0/4/#0,0\\//4380/4.0/5/-/1/1/#0,0",
    "ewExecutionInfo": "c:4380:7:161:162:161:n:::12473:200|C:4380:3:0:4:0:n:::6967:200|R:4380:20:99:99:1:n:::35982:200",
    "customField": "any-custom-value"
  }
}
```

## Sample Queries in ElasticSearch

Queries below assume you have named the ElasticSearch index as 'datastream2'.

### Get count of Records in Index

GET datastream2/\_count

Sample response:
[img](/resources/elastic_count_query_response.jpg)

```
{
  "count": 3005,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  }
}
```

### Get count of records for subset of data

```
GET datastream2/_search
{"size":"0",
   "query":{
    "match":{
      "country": "RU"
    }
  },
"aggs":{
  "count_bytes":{
    "value_count": {
      "field": "totalBytes"
    }
  }
}
}
```

Sample Response [img](/resources/elastic_agg_filter_example.jpg)

```
{
  "took": 0,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 64,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "count_bytes": {
      "value": 64
    }
  }
}
```
