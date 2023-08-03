```python
import ipfshttpclient

class IPFSClient:
    def __init__(self):
        self.client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')

    def add_file(self, file_path):
        res = self.client.add(file_path)
        return res

    def get_file(self, file_hash):
        self.client.get(file_hash)

    def cat_file(self, file_hash):
        return self.client.cat(file_hash)

    def pin_file(self, file_hash):
        self.client.pin.add(file_hash)

    def unpin_file(self, file_hash):
        self.client.pin.rm(file_hash)

    def close_connection(self):
        self.client.close()
```