#!/usr/bin/env python3
"""
This script changes all topics of a school
document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    ARGS:
        - mongo_collection: MongoDB collection object.
        - name: (string) will be the school name to update
        - topics: (list of strings) will be the list of
        topics approached in the school.
    """
    update = mongo_collection.update_many(
                {'name': name},
                {'$set': {'topics': topics}}
    )
