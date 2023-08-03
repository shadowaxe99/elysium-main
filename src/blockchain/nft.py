```python
from web3 import Web3
from solc import compile_source
from web3.contract import ConciseContract

class NFT:
    def __init__(self, contract_address, private_key):
        self.contract_address = contract_address
        self.private_key = private_key
        self.w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
        self.w3.eth.defaultAccount = self.w3.eth.accounts[0]

    def compile_contract(self, contract_source_code):
        compiled_sol = compile_source(contract_source_code)
        contract_interface = compiled_sol['<stdin>:NFT']

        return contract_interface

    def deploy_contract(self, contract_interface):
        contract = self.w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
        tx_hash = contract.constructor().transact()
        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        return tx_receipt

    def interact_with_contract(self, contract_interface, tx_receipt):
        contract = self.w3.eth.contract(
            address=tx_receipt['contractAddress'],
            abi=contract_interface['abi'],
        )
        return contract

    def mint_nft(self, contract, to, token_uri):
        tx_hash = contract.functions.mint(to, token_uri).transact()
        receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        return receipt

    def transfer_nft(self, contract, from_, to, token_id):
        tx_hash = contract.functions.transferFrom(from_, to, token_id).transact()
        receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)
        return receipt
```