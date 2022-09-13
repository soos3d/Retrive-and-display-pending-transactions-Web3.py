from web3 import Web3                            # Import the web3 library at the top.

node_url = input('Insert your Node URL: ')       # Accepts the user node URL.
web3 = Web3(Web3.HTTPProvider(node_url))         # Establish connection to the node.

# Verify if the connection is successful. This is optional, but it's nice to notify the user.
if web3.isConnected():                                                          
    print('Connection Successful')
else:
    print('Connection Failed')

# Display the latest block. This is optional, but it's nice to add this info for the user.
print('The latest block number is: ', str(web3.eth.blockNumber) + '\n') 

# retrive pending transactions hash
pending_tx_filter = web3.eth.filter('pending')
pending_tx = pending_tx_filter.get_new_entries()     # This is a list object.

# Loop through the list of transactions and display the tx hash.
for hash in pending_tx:
    print('Hash of a Pending Transaction:' , web3.toHex(hash))
