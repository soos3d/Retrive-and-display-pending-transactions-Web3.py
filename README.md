# Retrive-and-display-pending-transactions-Web3.py
This script allows a user to input an HTTPS endpoint for a network based on the EVM, then displays:
- Latest block number;
- List of pending transaction hash.<br>

You can check my Skillshare class where I elaborate more on this! WEB3.py: Interact with the Blockchain<br>
Get 30 days for free using this link! https://skl.sh/3McEymV

This program has been designed using the Web3.py library and the instructions to install the and use the library can be found at https://web3py.readthedocs.io/en/stable/quickstart.html#installation

<b>What is Web3.py?</b>

Web3.py is a Python library for interacting with the Ethereum network (Or other networks based on the EVM).

It’s commonly found in decentralized apps (dapps) to help with sending transactions, interacting with smart contracts, reading block data, and a variety of other use cases.

The original API was derived from the Web3.js Javascript API but has since evolved toward the needs and creature comforts of Python developers.
(source: Web3.py docs)

<b>How do I use this program to retrieve pending transactions?</b>

<b>1</b> - The Web3.py library must be installed in your environment. 

Run this code to install it in your enviroment:

``` sh
pip install web3
```

> **Note** that on Windows, you will need to install the [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) to make it work.

<b>2</b> - Have access to an HTTPS endpoint that allows creating the connection to the EVM.
    For the connection, it is recommended to use the service provided by chainstack.com, where you can create your personal node on the cloud. You can register and create one node for free. This is the recommended option as not all the HTTPS endpoints that can be found online support the methods that can be used through Web3.py.
    ![Yellow Magenta Black White Neon Scifi YouTube Intro (1)](https://user-images.githubusercontent.com/99700157/162478127-94cd2344-72f1-4136-a220-8b2c8e52d194.png)

<b>3</b> - Run the script and input your HTTPS endpoint URL where the program prompts it:
    ![b62be480-45d2-11ea-9989-803db0f9c44d](https://user-images.githubusercontent.com/99700157/162473751-ed2eb8b5-2218-487c-8f78-d7b3092539ff.png)
    
<b>4</b> - The program will try to connect and give a message to the user specifying if the connection was successful or if the connection failed.
![Yellow Magenta Black White Neon Scifi YouTube Intro (2)](https://user-images.githubusercontent.com/99700157/162474308-e83ae968-4752-492a-8573-4259ee341236.png)
    
<b>5</b> - If the connection was successful, it will display the latest block number and a list of pending transactions.
    ![Yellow Magenta Black White Neon Scifi YouTube Intro (2)](https://user-images.githubusercontent.com/99700157/162474607-04d754ba-a882-48d3-8145-2f9be4eb6fe9.png)   

<b>Now you can look up the transaction hash on the chain explorer!</b>
