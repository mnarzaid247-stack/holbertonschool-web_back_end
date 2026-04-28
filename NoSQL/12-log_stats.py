#!/usr/bin/env python3
"""Nginx logs stats"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    collection = client.logs.nginx

    print("{} logs".format(collection.count()))
    print("Methods:")

    print("	method GET: {}".format(collection.count({"method": "GET"})))
    print("	method POST: {}".format(collection.count({"method": "POST"})))
    print("	method PUT: {}".format(collection.count({"method": "PUT"})))
    print("	method PATCH: {}".format(collection.count({"method": "PATCH"})))
    print("	method DELETE: {}".format(collection.count({"method": "DELETE"})))

    print("{} status check".format(
        collection.count({"method": "GET", "path": "/status"})
    ))