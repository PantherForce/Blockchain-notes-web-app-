from flask import Flask, jsonify, request
from web3 import Web3
import os
from dotenv import load_dotenv
from notes_contract import Notes
from flask_cors import CORS

load_dotenv()

contract_address = os.getenv("CONTRACT_ADDRESS")
if not contract_address:
    raise ValueError("Contract address not found. Please set it in the .env file or provide it manually.")

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.default_account = web3.eth.accounts[0]

app = Flask(__name__)
CORS(app) 

notes_contract = Notes(web3, contract_address)

@app.route('/store_note', methods=['POST'])
def store_note():
    try:
        request_data = request.get_json()
        note = request_data.get('note')
        
        if not note:
            return jsonify({'error': 'Note not provided'}), 400
        
        tx_receipt = notes_contract.store_note(note)
        return jsonify({'message': f'Note stored successfully', 'transaction_receipt': str(tx_receipt)}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_note', methods=['GET'])
def get_note():
    try:
        stored_note = notes_contract.get_note()
        return jsonify({'note': stored_note}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/')
def home():
    return "<h1>Welcome to Notes DApp Backend!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
