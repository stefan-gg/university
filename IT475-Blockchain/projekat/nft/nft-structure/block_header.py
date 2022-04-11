from datetime import datetime
import hashlib

class BlockHeader:
    def __init__(self, previous_hash, difficulty_target, nonce, block_data):
        self.previous_hash = previous_hash
        self.timestamp = datetime.now()
        self.difficulty_target = difficulty_target
        self.nonce = nonce
        self.block_hash = self.set_block_hash()
        self.block_data = block_data

    def set_block_hash(self):
        str_to_hash = self.previous_hash + ' ' + str(self.timestamp) + ' ' + str(self.difficulty_target) + ' ' + str(self.nonce) + ' ' + str(self.block_data)
        hashed_value = hashlib.sha256(str_to_hash.encode('utf-8')).hexdigest()
        return hashed_value