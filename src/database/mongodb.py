```python
from pymongo import MongoClient

class MongoDB:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def insert_one(self, collection, document):
        return self.db[collection].insert_one(document).inserted_id

    def find_one(self, collection, query):
        return self.db[collection].find_one(query)

    def find(self, collection, query):
        return self.db[collection].find(query)

    def update_one(self, collection, query, new_values):
        return self.db[collection].update_one(query, {"$set": new_values})

    def delete_one(self, collection, query):
        return self.db[collection].delete_one(query)

    def close_connection(self):
        self.client.close()
```