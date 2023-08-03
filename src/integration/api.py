```python
import requests

class APIIntegration:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_request(self, endpoint):
        response = requests.get(self.base_url + endpoint)
        return response.json()

    def post_request(self, endpoint, data):
        response = requests.post(self.base_url + endpoint, data=data)
        return response.json()

    def put_request(self, endpoint, data):
        response = requests.put(self.base_url + endpoint, data=data)
        return response.json()

    def delete_request(self, endpoint):
        response = requests.delete(self.base_url + endpoint)
        return response.json()
```