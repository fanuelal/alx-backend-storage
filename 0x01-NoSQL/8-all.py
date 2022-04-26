#!/usr/bin/env python3
"""Module for listing all document"""
import pymongo


def list_all(mongo_collection):
    """returns lists of all documents"""
    
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
