#!/usr/bin/env python3
"""
This script adds the top 10 of the most present IPs in
the collection Nginx of the database logs.
"""

from pymongo import MongoClient


def main():
    """
    This function interacts with the MongoDB collection
    containing Nginx logs.
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
    print(f"{status_check_count} status check")

    # Aggregation query for top 10 IPs
    print("IPs:")
    request_logs = collection.aggregate(
            [
                {'$group': {'_id': '$ip', 'totalRequests': {'$sum': 1}}},
                {'$sort': {'totalRequests': -1}},
                {'$limit': 10}
            ]
    )

    # Print the IPs
    for request_log in request_logs:
        ip = request_log['_id']
        ip_requests_count = request_log['totalRequests']
        print(f"\t{ip}: {ip_requests_count}")


if __name__ == '__main__':
    main()
