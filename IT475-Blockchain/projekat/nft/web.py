from web3 import Web3

ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))
#provera konekcije
print(web3.isConnected())

account_1 = "0x5BF2458511f404E48cD97461f8b8060e678FA87b"
account_2 = "0xd89771ae5ed5ED1B98D1092049516aeBfDebf78c"
#preko privatnog ključa proveravamo dal je ok
#da se šalje 
private_key = "87aa2ec273361ad324fedac677964648f7237d8425120fba07bddf6d6fb68414"

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