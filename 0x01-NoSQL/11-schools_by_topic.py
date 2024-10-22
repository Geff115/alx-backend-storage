#!/usr/bin/env python3
"""
This script returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    ARGS:
        - mongo_collection: MongoDB collection object.
        - topic: (string) will be topic searched

    RETURN: A list of school having the specific topic.
    """
    topics = [school for school in mongo_collection.find({'topics': topic})]

    if not topics:
        return []
    else:
        return topics
