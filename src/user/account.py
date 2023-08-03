```python
from pymongo import MongoClient
from bson.objectid import ObjectId

class UserAccount:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['elysium']
        self.collection = self.db['users']

    def create_account(self, username, password, email):
        user = {
            "username": username,
            "password": password,
            "email": email,
            "ai_agents": []
        }
        return self.collection.insert_one(user).inserted_id

    def login(self, username, password):
        user = self.collection.find_one({"username": username, "password": password})
        if user:
            return True, user["_id"]
        else:
            return False, None

    def update_profile(self, user_id, new_data):
        self.collection.update_one({"_id": ObjectId(user_id)}, {"$set": new_data})

    def delete_account(self, user_id):
        self.collection.delete_one({"_id": ObjectId(user_id)})

    def add_ai_agent(self, user_id, ai_agent_id):
        self.collection.update_one({"_id": ObjectId(user_id)}, {"$push": {"ai_agents": ai_agent_id}})

    def remove_ai_agent(self, user_id, ai_agent_id):
        self.collection.update_one({"_id": ObjectId(user_id)}, {"$pull": {"ai_agents": ai_agent_id}})
```