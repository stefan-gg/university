from blockchain import BlockChain
from block import Block
from genesis_block import GenesisBlock

data_for_genesis = {'data': ["transaction1", "transaction2", "transation3"]}
genesis_block = GenesisBlock(data_for_genesis)

data_for_first_block = [genesis_block, {"data" : ["transaction1231", "transaction2141"]}]
first_block = Block(data_for_first_block[0], data_for_first_block[1])

data_for_second_block = [first_block, {"data" : ["transaction987", "transaction91241"]}]
second_block = Block(data_for_second_block[0], data_for_second_block[1])

chain_data = [genesis_block, first_block, second_block]

chain = BlockChain([])
chain.insert_genesis_block(chain_data[0])
for i in range(0, len(chain_data)):
    chain.insert_block(chain_data[i])

chain.print_chain()