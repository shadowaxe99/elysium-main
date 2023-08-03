```python
from web3 import Web3
from src.blockchain.ethereum import Ethereum
from src.user.account import UserAccount
from src.ai.agent import AIAgent

class Transaction:
    def __init__(self, provider: str):
        self.web3 = Web3(Web3.HTTPProvider(provider))
        self.ethereum = Ethereum(self.web3)

    def buy_agent(self, buyer: UserAccount, seller: UserAccount, agent: AIAgent, price: float):
        transaction = {
            'from': buyer.address,
            'to': seller.address,
            'value': self.web3.toWei(price, 'ether')
        }

        # Transfer ownership of the AI agent
        agent.transfer_ownership(buyer)

        # Execute the transaction
        self.ethereum.execute_transaction(transaction)

    def sell_agent(self, seller: UserAccount, agent: AIAgent, price: float):
        # List the AI agent for sale
        agent.list_for_sale(price)

    def transfer_agent(self, sender: UserAccount, receiver: UserAccount, agent: AIAgent):
        transaction = {
            'from': sender.address,
            'to': receiver.address,
            'value': 0  # No ether is being transferred
        }

        # Transfer ownership of the AI agent
        agent.transfer_ownership(receiver)

        # Execute the transaction
        self.ethereum.execute_transaction(transaction)
```