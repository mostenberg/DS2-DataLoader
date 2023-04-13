# Elasticsearch Sample DataStream2 Queries

## Overview

DataStream2 is Akamai's Edge Server Data Streaming product. It will send JSON data to analysis endpoints such as Elastic Search. DataStream2 has a variety of available fields which may be sent. Full list of fields is [here](https://techdocs.akamai.com/datastream2/v2/reference/data-set-fields-1) , and additional fields are available for different Akamai products.

[Elasticsearch](https://www.elastic.co/elasticsearch/) is a RESTful search and analytics engine which allows you to query and report on your data. It uses it's own query syntax to allow you to capture and analyze data.

This document contains some sample queries which will help illustrate how to use Elasticsearch queries to capture information from DataStream2 data

## Sample DataStream2 Data

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

Queries below assume you have named the ElasticSearch index as 'datastream2', and provide samples of how to do some useful queries against the DataStream2 dataset.

### Get count of records

```
GET datastream2/_count
```

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

---

### Get count of records with filter

Filter response to only those items which match a query.

```
GET /datastream2/_count
{
  "query":
  {"match": {
    "country": "US"}
  }
}
```

Sample response:

```
{
  "count": 77,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  }
}
```

---

GET Total count aggregated by country

```

GET datastream2/_search
{"size": 0,
  "aggs": {
    "hits_per_country": {
      "terms": {
        "field": "country",
        "size": 4
      }
    }
  }
}

```

Sample response:

```
{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 3002,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "hits_per_country": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 1745,
      "buckets": [
        {
          "key": "RU",
          "doc_count": 694
        },
        {
          "key": "KP",
          "doc_count": 350
        },
        {
          "key": "AT",
          "doc_count": 112
        },
        {
          "key": "FI",
          "doc_count": 99
        }
      ]
    }
  }
}
```

---

### Get sum of totalBytes delivered

```
GET /datastream2/_search
{
  "size": 0,
   "aggs":{"sum_bytes":{"sum": {
  "field": "totalBytes"
}}}
}
```

Sample response:

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
      "value": 3002,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "sum_bytes": {
      "value": 673687830
    }
  }
}
```

### Get sum of totalBytes filtered to a country

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
    "sum": {
      "field": "totalBytes"
    }
  }
}
}
```

Sample Response:

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
      "value": 694,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "count_bytes": {
      "value": 226634861
    }
  }
}
```

---

### Get count of totalBytes per country (limited to 4 countries)

```
GET datastream2/_search
{
  "size": "0",
  "aggs": {
    "bytes_per_country": {
      "terms": {
        "field": "country",
        "size": 4
      }
    }
  }
}
```

Sample response:

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
      "value": 3002,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "bytes_per_country": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 1745,
      "buckets": [
        {
          "key": "RU",
          "doc_count": 694
        },
        {
          "key": "KP",
          "doc_count": 350
        },
        {
          "key": "AT",
          "doc_count": 112
        },
        {
          "key": "FI",
          "doc_count": 99
        }
      ]
    }
  }
}
```

---

### Get sum of totalBytes per country limited to 4 countries

```
GET datastream2/_search
{
  "size": "0",
  "aggs": {
    "bytes_per_country": {
      "terms": {
        "field": "country",
        "size": 4
      },"aggs": {
        "sumOf_totalBytes": {
          "sum": {"field": "totalBytes"}
        }
      }
    }
  }
}
```

Sample Response:

```
{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 3002,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "bytes_per_country": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 1745,
      "buckets": [
        {
          "key": "RU",
          "doc_count": 694,
          "sumOf_totalBytes": {
            "value": 226634861
          }
        },
        {
          "key": "KP",
          "doc_count": 350,
          "sumOf_totalBytes": {
            "value": 116886964
          }
        },
        {
          "key": "AT",
          "doc_count": 112,
          "sumOf_totalBytes": {
            "value": 19536356
          }
        },
        {
          "key": "FI",
          "doc_count": 99,
          "sumOf_totalBytes": {
            "value": 16127936
          }
        }
      ]
    }
  }
}
```

---

### Calculate offload per country

```

POST /datastream2/_search
{
  "size": 0,
  "aggs": {
    "offload_by_country": {
      "terms": {
        "field": "country",
        "size": 4
      },
      "aggs": {
        "cache_hits": {
          "filter": {
            "term": {
              "cacheStatus": "1"
            }
          }
        },
        "edge_hits": {
          "value_count": {
            "field": "cacheStatus"
          }
        },
        "offload": {
          "bucket_script": {
            "buckets_path": {
              "cacheHits": "cache_hits._count",
              "edgeHits": "edge_hits.value"
            },
            "script": "params.cacheHits > 0 ? params.cacheHits / params.edgeHits * 100 : 0"
          }
        }
      }
    }
  }
}
```

Sample response:

```

POST /datastream2/_search
{
  "size": 0,
  "aggs": {
    "offload_by_country": {
      "terms": {
        "field": "country",
        "size": 10
      },
      "aggs": {
        "cache_hits": {
          "filter": {
            "term": {
              "cacheStatus": "1"
            }
          }
        },
        "edge_hits": {
          "value_count": {
            "field": "cacheStatus"
          }
        },
        "offload": {
          "bucket_script": {
            "buckets_path": {
              "cacheHits": "cache_hits._count",
              "edgeHits": "edge_hits.value"
            },
            "script": "params.cacheHits > 0 ? params.cacheHits / params.edgeHits * 100 : 0"
          }
        }
      }
    }
  }
}
```

---

### Calculate offload by resource

```

POST /datastream2/_search
{
  "size": 0,
  "aggs": {
    "offload_by_resource": {
      "terms": {
        "field": "reqPath",
        "size": 4
      },
      "aggs": {
        "cache_hits": {
          "filter": {
            "term": {
              "cacheStatus": "1"
            }
          }
        },
        "edge_hits": {
          "value_count": {
            "field": "cacheStatus"
          }
        },
        "offload": {
          "bucket_script": {
            "buckets_path": {
              "cacheHits": "cache_hits._count",
              "edgeHits": "edge_hits.value"
            },
            "script": "params.cacheHits > 0 ? params.cacheHits / params.edgeHits * 100 : 0"
          }
        }
      }
    }
  }
}
```

Sample response:

```
{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 3002,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "offload_by_resource": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 1639,
      "buckets": [
        {
          "key": "/another/animation.gif",
          "doc_count": 363,
          "cache_hits": {
            "doc_count": 273
          },
          "edge_hits": {
            "value": 363
          },
          "offload": {
            "value": 75.20661157024794
          }
        },
        {
          "key": "/big/file/movie.mpg",
          "doc_count": 335,
          "cache_hits": {
            "doc_count": 251
          },
          "edge_hits": {
            "value": 335
          },
          "offload": {
            "value": 74.92537313432835
          }
        },
        {
          "key": "/fancy/movie.mpg",
          "doc_count": 334,
          "cache_hits": {
            "doc_count": 246
          },
          "edge_hits": {
            "value": 334
          },
          "offload": {
            "value": 73.65269461077844
          }
        },
        {
          "key": "/my/animated/file.gif",
          "doc_count": 329,
          "cache_hits": {
            "doc_count": 232
          },
          "edge_hits": {
            "value": 329
          },
          "offload": {
            "value": 70.51671732522796
          }
        }
      ]
    }
  }
}
```
