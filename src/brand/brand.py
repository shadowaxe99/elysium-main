```python
class Brand:
    def __init__(self, brand_id, brand_name, brand_description):
        self.brand_id = brand_id
        self.brand_name = brand_name
        self.brand_description = brand_description
        self.branded_ai_agents = []

    def create_branded_ai_agent(self, ai_agent):
        self.branded_ai_agents.append(ai_agent)

    def get_branded_ai_agents(self):
        return self.branded_ai_agents

    def get_brand_info(self):
        return {
            "brand_id": self.brand_id,
            "brand_name": self.brand_name,
            "brand_description": self.brand_description
        }
```