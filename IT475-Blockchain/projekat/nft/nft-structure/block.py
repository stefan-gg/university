from block_header import BlockHeader
from transaction import Transaction
class Block():
    def __init__(self, block_header: BlockHeader, trasaction: Transaction):
        self.block_header = block_header
        self.transaction = trasaction
    
    def __str__(self):
        return "Block header: " + str(self.block_header) + ", Transaction: " + str(self.transaction)