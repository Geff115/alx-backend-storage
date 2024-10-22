#!/usr/bin/env python3
"""
This script interacts with the MongoDB collection
containing Nginx logs.
"""

from pymongo import MongoClient


def main():
    """
    This function interacts with the MongoDB collection
    containing Nginx logs
    """
    # Connect to the MongoDB database
    client = MongoClient('mongodb://localhost:27017')
    # Accessing the Nginx collection in 'logs' db
    collection = client.logs.nginx

    # Counting the total logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Counting the methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Counting the status
    status_check_count = collection.count_documents(
             {"method": "GET", "path": "/status"}
    )
    print(status_check_count, "status check")


if __name__ == '__main__':
    main()
