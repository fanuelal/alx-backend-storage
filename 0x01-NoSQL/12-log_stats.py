#!/usr/bin/env python3
"""Module status logs"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.0.1:27017")
    log_collection = client.logs.nginx

    print("{} logs".format(log_collection.estimated_document_count()))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print("method []: []"
              .format(method,
                      log_collection.count_documents({'method': method})))

    print("{} status check".format(
        log_collection.count_documents({'method': "GET", 'path': "/status"})))
