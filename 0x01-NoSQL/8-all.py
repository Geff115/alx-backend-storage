#!/usr/bin/env python3
"""
This script lists all documents in a
collection.
"""


def list_all(mongo_collection):
    """
    ARGS:
        - mongo_collection: A MongoDB collection(i.e documents)

    RETURN: A list of all documents in the collection
    """
    return [list_doc for list_doc in mongo_collection.find()]
