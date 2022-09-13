# Retrive and display pending transactions using Web3.py

## Introduction

Retrieving pending transactions is a helpful concept; let's see how to retrieve the pending transactions and display the transaction hash using web3.py!

The script we'll create in this tutorial allows a user to input an HTTPS endpoint for an EVM-based network, then displays:
- Latest block number;
- List of pending transaction hash.

After that, you can take the hashes and analyze them or do what you wish with some Python logic.

> The code is commented to that you can understand what we do and why!

> You can also check my Skillshare class where I elaborate more on this! 

### WEB3.py: Interact with the Blockchain

[Get 30 days for free on Skillshare using this link!](https://skl.sh/3McEymV)

## Table of contents


  - [Introduction](#introduction)
    - [WEB3.py: Interact with the Blockchain](#web3py-interact-with-the-blockchain)
  - [Requirements](#requirements)
  - [What is Web3.py?](#what-is-web3py)
  - [Explore the code](#explore-the-code)
    - [Connect to the node](#connect-to-the-node)
    - [Use a filter to retrieve pending transactions](#use-a-filter-to-retrieve-pending-transactions)
    - [Extract the transaction hashes](#extract-the-transaction-hashes)
  - [Run the script](#run-the-script)
  - [Conclusion](#conclusion)

## Requirements 

This program has been designed using the `Web3.py` library, you will need to install the following: 

- [Python](https://www.python.org/downloads/).
- [web3.py library](https://web3py.readthedocs.io/en/stable/quickstart.html)

You can install `web3.py` after installing Python with:

```sh
pip install web3
```

> **Note** that on Windows, you will need to install the [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) to make it work.

Then you need access to a node endpoint to connect to the blockchain from which you want to get pending transactions.

To access a node endpoint, I recommend using [Chainstack](https://chainstack.com/):

Follow these steps to sign up on Chainstack, deploy a node, and find your endpoint credentials:

  1. [Sign up with Chainstack](https://console.chainstack.com/user/account/create).
  1. [Deploy a node](https://docs.chainstack.com/platform/join-a-public-network).
  1. [View node access and credentials](https://docs.chainstack.com/platform/view-node-access-and-credentials).


## What is Web3.py?

Web3.py is a Python library for interacting with the Ethereum network (Or other networks based on the EVM).

It’s commonly found in decentralized apps (dapps) to help with sending transactions, interacting with smart contracts, reading block data, and a variety of other use cases.

The original API was derived from the Web3.js Javascript API but has since evolved toward the needs and creature comforts of Python developers.

* source: [Web3.py docs](https://web3py.readthedocs.io/en/stable/)

## Explore the code

The code is very Python fashion and is absolutely straightforward. The script can be divided into three sections:

1. Establish a connection to the node by inserting the node URL.
1. Use a filter to retrieve pending transactions.
1. Loop through the list of pending transactions returned by the filter and display the hashed on the console.

Let's start by creating a new Python file in your project's folder; I named it `pending_tx.py`.

### Connect to the node

The first part of the script is to establish a connection to the node; for this, we use the following code.

> **Note:** In this case, we ask the user for an input, so you can use the URL you want at that moment since you can use this script with any EVM-compatible network, but you can also hardcode the URL.

```py
from web3 import Web3                            # Import the web3 library at the top.

node_url = input('Insert your Node URL: ')       # Accepts the user node URL.
web3 = Web3(Web3.HTTPProvider(node_url))         # Establish connection to the node.

# Verify if the connection is successful. This is optional, but it's nice to notify the user.
if web3.isConnected():                                                          
    print('Connection Successful')
else:
    print('Connection Failed')
```

### Use a filter to retrieve pending transactions

The next step is to use a filter to retrieve the pending transactions.

```py
# Display the latest block. This is optional, but it's nice to add this info for the user.
print('The latest block number is: ', str(web3.eth.blockNumber) + '\n') 

# Retrive pending transactions hash using a filter.
pending_tx_filter = web3.eth.filter('pending')
pending_tx = pending_tx_filter.get_new_entries()     # This is a list object.
```

This is now returning a list of the pending transactions in the mempool. 

### Extract the transaction hashes

The last step is to take the hashes from our list. We simply loop through the list, take the hash, convert it into HEX, and display it on the console.

```py
# loop through the list of transactions and display the tx hash.
for hash in pending_tx:
    print('Hash of a Pending Transaction:' , web3.toHex(hash))
```

That's it! So simple; at this point, we just need to run it.

## Run the script

To run the program, open a console in the folder where you saved the Python file and run:

```sh
python pending_tx.py
```

Input your HTTPS endpoint URL where the program prompts it:

![screely-1663077686544](https://user-images.githubusercontent.com/99700157/189921742-f1f28b19-81d0-4dd2-a16f-b14b32a8de82.png)
    
The program will try to connect and give a message to the user specifying if the connection was successful or failed.

![screely-1663077664372](https://user-images.githubusercontent.com/99700157/189921989-89035f93-b004-4fbb-b17f-c74bb38583a3.png)
    
The console will display the latest block number and a list of pending transactions if the connection is successful.

![screely-1663077676514](https://user-images.githubusercontent.com/99700157/189922250-570eeccf-824b-4df5-8d6f-0e7dc4b51cf4.png)

Now you can look up the transaction hash on the chain explorer or include some more Python logic to extracts the data that you need!

## Conclusion

This simple script can retrieve pending transaction hashes from the mempool, but most importantly, it's an excellent way to learn how to use web3.py to interact with a blockchain!
