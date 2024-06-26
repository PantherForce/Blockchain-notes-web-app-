from web3 import Web3
from web3.contract import Contract
import os
from dotenv import load_dotenv

load_dotenv()

abi = [
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_note",
                "type": "string"
            }
        ],
        "name": "storeNote",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getNote",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "constant": "true"
    }
]

class Notes:
    def __init__(self, web3: Web3, contract_address: str):
        self.web3 = web3
        self.contract_address = contract_address
        self.contract = web3.eth.contract(address=contract_address, abi=abi)

    def store_note(self, note: str):
        tx_hash = self.contract.functions.storeNote(note).transact({'from': self.web3.eth.default_account})
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        return tx_receipt

    def get_note(self):
        stored_note = self.contract.functions.getNote().call({'from': self.web3.eth.default_account})
        return stored_note
