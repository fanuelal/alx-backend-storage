#!/usr/bin/env python3
"""Module updating documents"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """function that changes all topics of a school"""
    if name == '':
        return None
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
