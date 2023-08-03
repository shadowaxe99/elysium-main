```python
from web3 import Web3
from solcx import compile_source

class Ethereum:
    def __init__(self, provider_url):
        self.web3 = Web3(Web3.HTTPProvider(provider_url))

    def is_connected(self):
        return self.web3.isConnected()

    def compile_contract(self, contract_source_code):
        compiled_sol = compile_source(contract_source_code)
        contract_id, contract_interface = compiled_sol.popitem()
        return contract_interface

    def deploy_contract(self, contract_interface, account, passphrase):
        contract = self.web3.eth.contract(
            abi=contract_interface['abi'], 
            bytecode=contract_interface['bin']
        )
        transaction = {
            'from': account,
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei')
        }
        tx_hash = contract.constructor().transact(transaction)
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        return tx_receipt

    def get_contract_instance(self, contract_interface, contract_address):
        contract = self.web3.eth.contract(
            abi=contract_interface['abi'],
            address=contract_address
        )
        return contract
```