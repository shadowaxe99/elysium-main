```python
import unittest
from src.storage import ipfs

class TestStorage(unittest.TestCase):

    def setUp(self):
        self.ipfs = ipfs.IPFS()

    def test_store_data(self):
        data = "Test data"
        hash = self.ipfs.store_data(data)
        self.assertIsNotNone(hash)

    def test_retrieve_data(self):
        data = "Test data"
        hash = self.ipfs.store_data(data)
        retrieved_data = self.ipfs.retrieve_data(hash)
        self.assertEqual(data, retrieved_data)

    def test_delete_data(self):
        data = "Test data"
        hash = self.ipfs.store_data(data)
        self.ipfs.delete_data(hash)
        retrieved_data = self.ipfs.retrieve_data(hash)
        self.assertIsNone(retrieved_data)

if __name__ == '__main__':
    unittest.main()
```