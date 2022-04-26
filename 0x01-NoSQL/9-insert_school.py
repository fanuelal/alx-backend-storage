#!/usr/bin/env python3
"""Module that inser new document in mongo"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document
    in a collection based"""
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
