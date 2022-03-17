class BlockChain:
    def __init__(self, chain):
        self.chain = chain

    def insert_genesis_block(self, genesis_block):
        if len(self.chain) == 0:
            self.chain.append(genesis_block)
        else:
            self.chain[0] = genesis_block

    def insert_block(self, block):
        self.chain.append(block);

    def print_chain(self):
        chain_string = ""
        
        for i in self.chain:
            if self.chain.index(i) != len(self.chain) - 1:
                chain_string += str(i) + " <--- "
            else:
                chain_string += str(i)

        print(chain_string)