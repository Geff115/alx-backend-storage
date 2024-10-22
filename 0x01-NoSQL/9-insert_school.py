#!/usr/bin/env python3
"""
This script inserts a new document in a collection
based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
    ARGS:
        - mongo_collection: A MongoDB collection(i.e documents)
        - **kwargs: A key-value argument to insert in the document.

    RETURN: The new id of the document.
    """
    insert_document = mongo_collection.insert_one(kwargs)

    return insert_document.inserted_id
