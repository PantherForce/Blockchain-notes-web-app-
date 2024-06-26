Notes DApp

This project is a decentralized application (DApp) that allows users to store and retrieve notes on a blockchain. It consists of a Solidity smart contract deployed on a local Ethereum test network (Ganache), a Python backend using Flask and Web3.py, and a frontend developed with HTML, CSS, and JavaScript.

Features

1. Store Note: Users can enter a note and store it securely on the blockchain.
2. Retrieve Note: Users can fetch the previously stored note from the blockchain.

Prerequisites

Before running the project, ensure you have the following installed:

1. Python (version 3.6 or higher)
2. Flask (pip install Flask)
3. Web3.py (pip install web3)
4. Ganache (or any local Ethereum blockchain for testing)
5. Node.js and npm (for installing web dependencies if needed)

Installation
Clone the repository:

git clone <repository-url>

cd notes-dapp/backend

Install Python dependencies:
pip install -r requirements.txt

Start Ganache:
Start your local Ethereum blockchain (Ganache) where the smart contract will be deployed.

Deploy the Smart Contract:
Compile your Solidity smart contract using Remix or Solidity Compiler.
Deploy the compiled contract to your local Ethereum network (Ganache).

Configure the Backend:
Modify config.py to set your Ethereum node URL (typically http://localhost:7545 for Ganache).
Update contract_address in .env with the deployed smart contract address.

Run the Backend:
python app.py

Run the Frontend:
Open index.html in your web browser.

Usage:
Enter a note in the input field and click Store Note to save it on the blockchain.
Click Get Note to retrieve the previously stored note.

Made with love ~ Likhith Reddy
