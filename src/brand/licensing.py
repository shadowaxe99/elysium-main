```python
from src.blockchain.ethereum import EthereumBlockchain
from src.blockchain.nft import NFT
from src.brand.brand import Brand
from src.user.account import UserAccount

class Licensing:
    def __init__(self):
        self.blockchain = EthereumBlockchain()
        self.nft = NFT()

    def license_brand_agent(self, brand: Brand, user_account: UserAccount):
        # Check if the brand has an AI agent
        if not brand.ai_agent:
            raise Exception("Brand does not have an AI agent")

        # Mint the AI agent as an NFT
        nft_token = self.nft.mint(brand.ai_agent)

        # Transfer the NFT to the user's account
        self.blockchain.transfer_nft(nft_token, user_account.address)

        return nft_token
```