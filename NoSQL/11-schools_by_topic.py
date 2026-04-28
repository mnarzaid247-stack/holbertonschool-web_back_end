#!/usr/bin/env python3
"""List schools by topic"""


def schools_by_topic(mongo_collection, topic):
    """returns list of schools having topic"""
    return list(mongo_collection.find({"topics": topic}))