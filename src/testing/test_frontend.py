```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FrontendTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_account_creation(self):
        driver = self.driver
        driver.get("http://localhost:3000/signup")
        self.assertIn("Elysium Innovations - Sign Up", driver.title)
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        username.send_keys("testuser")
        password.send_keys("testpassword")
        password.send_keys(Keys.RETURN)
        self.assertIn("Account successfully created", driver.page_source)

    def test_login(self):
        driver = self.driver
        driver.get("http://localhost:3000/login")
        self.assertIn("Elysium Innovations - Login", driver.title)
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        username.send_keys("testuser")
        password.send_keys("testpassword")
        password.send_keys(Keys.RETURN)
        self.assertIn("Logged in successfully", driver.page_source)

    def test_ai_agent_creation(self):
        driver = self.driver
        driver.get("http://localhost:3000/ai-agent-creation")
        self.assertIn("Elysium Innovations - AI Agent Creation", driver.title)
        agent_name = driver.find_element_by_name("agent_name")
        agent_name.send_keys("testagent")
        agent_name.send_keys(Keys.RETURN)
        self.assertIn("AI Agent successfully created", driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
```