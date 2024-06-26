![Screenshot (554)](https://github.com/PantherForce/Blockchain-notes-web-app-/assets/114012972/4bc4f5e3-6e18-4e73-94dd-7368bb4421d4)

Basic Frontend of our project

![Screenshot (555)](https://github.com/PantherForce/Blockchain-notes-web-app-/assets/114012972/93f2e9af-bb42-48ac-89eb-02a5c8b8b350)

here you can see i have 44 current block in ganache engine.

![Screenshot (556)](https://github.com/PantherForce/Blockchain-notes-web-app-/assets/114012972/5469f696-7908-45ae-907a-60e843ad3b93)

Now i am entering nokia as my note and clicking on store note button.

![Screenshot (557)](https://github.com/PantherForce/Blockchain-notes-web-app-/assets/114012972/9fb4dfea-2d6a-49de-a498-f322af6c299f)

My transcation was sucessfull here you can see and you can see my current block is 45 now .

![Screenshot (558)](https://github.com/PantherForce/Blockchain-notes-web-app-/assets/114012972/83308dfd-aea3-468c-8969-705eb3a1305f)

Upon clicking on get note you can see the note which you saved.

Notes DApp : This project is a decentralized application (DApp) that allows users to store and retrieve notes on a blockchain. It consists of a Solidity smart contract deployed on a local Ethereum test network (Ganache), a Python backend using Flask and Web3.py, and a frontend developed with HTML, CSS, and JavaScript.

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

Made with love ~ Likhith Reddy :)
