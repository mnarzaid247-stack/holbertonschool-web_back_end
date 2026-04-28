#!/usr/bin/env python3
"""Nginx logs stats"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    collection = client.logs.nginx

    print("{} logs".format(collection.count()))
    print("Methods:")

    print("\tmethod GET: {}".format(collection.count({"method": "GET"})))
    print("\tmethod POST: {}".format(collection.count({"method": "POST"})))
    print("\tmethod PUT: {}".format(collection.count({"method": "PUT"})))
    print("\tmethod PATCH: {}".format(collection.count({"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(collection.count({"method": "DELETE"})))

    print("{} status check".format(
        collection.count({"method": "GET", "path": "/status"})
    ))