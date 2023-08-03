```python
import unittest
from src.user.account import UserAccount
from src.user.authentication import UserAuthentication
from src.user.subscription import UserSubscription

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user_account = UserAccount()
        self.user_auth = UserAuthentication()
        self.user_sub = UserSubscription()

    def test_account_creation(self):
        response = self.user_account.create_account('test_username', 'test_password')
        self.assertEqual(response['status'], 'success')

    def test_account_login(self):
        response = self.user_auth.login('test_username', 'test_password')
        self.assertEqual(response['status'], 'success')

    def test_account_subscription(self):
        response = self.user_sub.subscribe('test_username')
        self.assertEqual(response['status'], 'success')

    def test_account_unsubscription(self):
        response = self.user_sub.unsubscribe('test_username')
        self.assertEqual(response['status'], 'success')

if __name__ == '__main__':
    unittest.main()
```