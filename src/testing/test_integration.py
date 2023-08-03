```python
import unittest
from src.integration.api import API
from src.integration.partnership import Partnership

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.api = API()
        self.partnership = Partnership()

    def test_api_connection(self):
        response = self.api.connect()
        self.assertEqual(response.status_code, 200)

    def test_api_data_retrieval(self):
        data = self.api.get_data()
        self.assertIsNotNone(data)

    def test_partnership_creation(self):
        response = self.partnership.create_partnership('Test Partner')
        self.assertEqual(response.status_code, 200)

    def test_partnership_data(self):
        data = self.partnership.get_partnership_data('Test Partner')
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()
```