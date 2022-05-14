from block_header import BlockHeader
from transaction import Transaction
class Block():
    def __init__(self, block_header: BlockHeader, trasaction: Transaction):
        self.block_header = block_header
        self.transaction = trasaction