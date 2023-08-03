```python
import unittest
from src.marketplace.marketplace import Marketplace
from src.marketplace.transaction import Transaction
from src.ai.agent import Agent
from src.user.account import User

class TestMarketplace(unittest.TestCase):

    def setUp(self):
        self.marketplace = Marketplace()
        self.user1 = User("user1", "password1")
        self.user2 = User("user2", "password2")
        self.agent1 = Agent("agent1", self.user1)
        self.transaction = Transaction(self.user1, self.user2, self.agent1)

    def test_list_agent(self):
        self.marketplace.list_agent(self.agent1, self.user1)
        self.assertIn(self.agent1, self.marketplace.listings)

    def test_remove_listing(self):
        self.marketplace.list_agent(self.agent1, self.user1)
        self.marketplace.remove_listing(self.agent1)
        self.assertNotIn(self.agent1, self.marketplace.listings)

    def test_buy_agent(self):
        self.marketplace.list_agent(self.agent1, self.user1)
        self.marketplace.buy_agent(self.agent1, self.user2)
        self.assertEqual(self.agent1.owner, self.user2)

    def test_transaction_history(self):
        self.marketplace.list_agent(self.agent1, self.user1)
        self.marketplace.buy_agent(self.agent1, self.user2)
        self.assertIn(self.transaction, self.marketplace.transaction_history)

if __name__ == '__main__':
    unittest.main()
```