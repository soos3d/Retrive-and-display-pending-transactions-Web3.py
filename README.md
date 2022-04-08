# Retrive-and-display-pending-transactions-Web3.py
This script allows a user to input an HTTPS endpoint for a network based on the EVM, then displays:
- Latest block number;
- List of pending transaction hash.

This program has been designed using the Web3.py library and the instructions to install the and use the library can be found at https://web3py.readthedocs.io/en/stable/quickstart.html#installation

What is Web3.py?

Web3.py is a Python library for interacting with the Ethereum network (Or other networks based on the EVM).

It’s commonly found in decentralized apps (dapps) to help with sending transactions, interacting with smart contracts, reading block data, and a variety of other use cases.

The original API was derived from the Web3.js Javascript API but has since evolved toward the needs and creature comforts of Python developers.
(source: Web3.py docs)

How do I use this program to retrieve pending transactions?

1 - The Web3.py library must be installed in your environment. 
2 - Have access to an HTTPS endpoint that allows creating the connection to the EVM.
    For the connection, it is recommended to use the service provided by chainstack.com, where you can create your personal node on the cloud. You can register and         create one node for free. This is the recommended option as not all the HTTPS endpoints that can be found online support the methods that can be used through           Web.py.
    ![chainstack](https://user-images.githubusercontent.com/99700157/162471441-485249dc-0d21-4c1d-9092-c3de6f6fab85.png)

    Create a free account here: https://console.chainstack.com/user/account/create
    
    Find your Endpoint URL:
    ![Yellow Magenta Black White Neon Scifi YouTube Intro (1)](https://user-images.githubusercontent.com/99700157/162473672-f207d240-becf-4107-a633-d85921e5222f.png)
    
3 - Run the script and input your HTTPS endpoint URL where the program prompts it:
    ![b62be480-45d2-11ea-9989-803db0f9c44d](https://user-images.githubusercontent.com/99700157/162473751-ed2eb8b5-2218-487c-8f78-d7b3092539ff.png)
    
4 - The program will try to connect and give a message to the user specifying if the connection was successful or if the connection failed.
    ![Yellow Magenta Black White Neon Scifi YouTube Intro (2)](https://user-images.githubusercontent.com/99700157/162474308-e83ae968-4752-492a-8573-4259ee341236.png)
    
5 - If the connection was successful, it will display the latest block number and a list of pending transactions.
    ![Yellow Magenta Black White Neon Scifi YouTube Intro (2)](https://user-images.githubusercontent.com/99700157/162474607-04d754ba-a882-48d3-8145-2f9be4eb6fe9.png)   

Now you can look up the transaction hash on the chain explorer!

