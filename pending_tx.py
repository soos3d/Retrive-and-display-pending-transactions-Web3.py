from web3 import Web3

node_url = input('Insert your BSC Node URL: ')   # accepts the user node URL
web3 = Web3(Web3.HTTPProvider(node_url))         # establish connection to the node

# verify if the connection is successful 
if web3.isConnected():                                                          
    print('Connection Succsessful')
else:
    print('Connection Failed')

# displays the latest block
print('The latest block number is: ', str(web3.eth.blockNumber) + '\n') 

# retrive pending transactions hash
pending_tx_filter = web3.eth.filter('pending')
pending_tx = pending_tx_filter.get_new_entries()     # this is a list object

# loop through the list of transcations and displays the tx hash
for hash in pending_tx:
    print('Hash of a Pending Transaction:' , web3.toHex(hash))
