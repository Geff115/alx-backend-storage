#!/usr/bin/env python3
"""
This script returns all students sorted by average score.
"""


def top_students(mongo_collection):
    """
    ARGS:
        - mongo_collection: MongoDB collection object.

    RETURN: A list of students sorted by average score.
    """
    students = mongo_collection.aggregate(
        [
            {
                '$unwind': '$topics'  # Deconstruct the topics array
            },
            {
                '$group': {
                    '_id': '$_id',  # Group by student ID
                    'name': {'$first': '$name'},  # Preserve student name
                    'averageScore': {'$avg': '$topics.score'}
                },
            },
            {
                '$sort': {'averageScore': -1}
            },
        ]
    )

    return list(students)  # Convert the cursor to a list to return
