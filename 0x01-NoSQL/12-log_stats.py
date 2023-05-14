#!/usr/bin/env python3

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.logs
collection = db.nginx

# Count documents in collection
count = collection.count_documents({})

# Print number of logs
print(f"{count} logs")

# Count logs by HTTP method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    method_count = collection.count_documents({"method": method})
    print(f"    method {method}: {method_count}")

# Count logs with method=GET and path=/status
status_count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_count} status check")
