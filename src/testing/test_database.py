```python
import unittest
from pymongo import MongoClient
from src.database import mongodb

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['test_database']
        self.collection = self.db['test_collection']
        self.mongodb = mongodb.MongoDB(self.db)

    def test_insert(self):
        data = {'name': 'test', 'value': 'test_value'}
        result = self.mongodb.insert(self.collection, data)
        self.assertIsNotNone(result)

    def test_find(self):
        data = {'name': 'test'}
        result = self.mongodb.find(self.collection, data)
        self.assertIsNotNone(result)

    def test_update(self):
        query = {'name': 'test'}
        new_data = {'$set': {'value': 'new_test_value'}}
        result = self.mongodb.update(self.collection, query, new_data)
        self.assertIsNotNone(result)

    def test_delete(self):
        query = {'name': 'test'}
        result = self.mongodb.delete(self.collection, query)
        self.assertIsNotNone(result)

    def tearDown(self):
        self.client.close()

if __name__ == '__main__':
    unittest.main()
```