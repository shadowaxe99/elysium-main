```python
from src.blockchain.ethereum import EthereumBlockchain
from src.blockchain.nft import NFT
from src.user.account import UserAccount
from src.ai.agent import AIAgent

class Marketplace:
    def __init__(self):
        self.blockchain = EthereumBlockchain()
        self.users = []
        self.ai_agents = []

    def add_user(self, user: UserAccount):
        self.users.append(user)

    def add_ai_agent(self, ai_agent: AIAgent):
        self.ai_agents.append(ai_agent)

    def list_ai_agent_for_sale(self, ai_agent: AIAgent, price: float):
        if ai_agent.owner is None:
            raise Exception("AI Agent must have an owner to be listed for sale.")
        if ai_agent not in self.ai_agents:
            raise Exception("AI Agent must be registered in the marketplace.")
        nft = NFT(ai_agent, price)
        self.blockchain.mint(nft)
        ai_agent.for_sale = True

    def buy_ai_agent(self, buyer: UserAccount, ai_agent: AIAgent):
        if ai_agent.for_sale is False:
            raise Exception("AI Agent is not for sale.")
        if buyer.balance < ai_agent.price:
            raise Exception("Buyer does not have enough balance.")
        buyer.balance -= ai_agent.price
        ai_agent.owner.balance += ai_agent.price
        ai_agent.owner = buyer
        ai_agent.for_sale = False
        self.blockchain.transfer(ai_agent.nft, buyer)

    def remove_ai_agent(self, ai_agent: AIAgent):
        if ai_agent in self.ai_agents:
            self.ai_agents.remove(ai_agent)
        else:
            raise Exception("AI Agent is not registered in the marketplace.")
```
