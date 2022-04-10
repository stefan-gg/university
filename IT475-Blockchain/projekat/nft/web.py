from web3 import Web3

ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))
#provera konekcije
print(web3.isConnected())

account_1 = "0xa09Ff79B07e23139821c80E2c4A5A2092DA782F0"
account_2 = "0x44f63E14fe2729dD5be91cF23A319773CD06386f"
#preko privatnog ključa proveravamo dal je ok
#da se šalje 
private_key = "3f2b512ad68e38cc6b69d0712f041c3c70643d234c3e3b6b3aa9600eda160d0d"

# build transaction
# sign transaction
# send
# hash

nonce = web3.eth.getTransactionCount(account_1)

transation = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 200000,
    'gasPrice': web3.toWei('50', 'gwei')
    #gwei > wei manje od etheriuma
    #nonce sprecava da se 2 puta transakcija posalje
}

signed_tr = web3.eth.account.signTransaction(transation, private_key)
tr_hash = web3.eth.sendRawTransaction(signed_tr.rawTransaction)
print(web3.toHex(tr_hash))