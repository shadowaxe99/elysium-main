```python
import unittest
from src.ai.agent import Agent
from src.ai.creation import create_agent
from src.ai.interaction import interact_with_agent
from src.ai.analysis import analyze_agent

class TestAI(unittest.TestCase):

    def setUp(self):
        self.agent_data = {
            "name": "Test Agent",
            "skin": "default",
            "services": ["analytics", "creative"]
        }
        self.agent = create_agent(self.agent_data)

    def test_agent_creation(self):
        self.assertIsInstance(self.agent, Agent)
        self.assertEqual(self.agent.name, self.agent_data["name"])
        self.assertEqual(self.agent.skin, self.agent_data["skin"])
        self.assertEqual(self.agent.services, self.agent_data["services"])

    def test_agent_interaction(self):
        interaction_result = interact_with_agent(self.agent, "Hello, Agent!")
        self.assertIsInstance(interaction_result, str)

    def test_agent_analysis(self):
        analysis_result = analyze_agent(self.agent)
        self.assertIsInstance(analysis_result, dict)
        self.assertIn("usage_stats", analysis_result)

    def tearDown(self):
        del self.agent

if __name__ == "__main__":
    unittest.main()
```