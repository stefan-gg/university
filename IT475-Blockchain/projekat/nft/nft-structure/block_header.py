from datetime import datetime
import hashlib

class BlockHeader:
    def __init__(self, previous_hash, difficulty_target: int, nonce: int, block_data):
        self.previous_hash = previous_hash
        self.timestamp = datetime.now()
        self.difficulty_target = difficulty_target
        self.nonce = nonce
        self.block_data = block_data
        self.block_hash = self.set_block_hash()
    
    def __str__(self):
        return "Previous hash: " + str(self.previous_hash) + ", Timestamp: " + str(self.timestamp) + ", Nonce: " + str(self.nonce) + ", Diff targer: " + str(self.difficulty_target) + ", Block data: " + str(self.block_data) + ", Block hash: " + str(self.block_hash)

    def validate_hash(self):

        hash = self.set_block_hash()

        if hash[:self.difficulty_target] == "0" * self.difficulty_target:
            return True
        else:
            return False

    #nova funkcija 
    def set_block_hash(self):
        hash_is_valid = False 
        hashed_value = ""

        while not hash_is_valid:

            str_to_hash = str(self.previous_hash) + str(self.timestamp) + str(self.difficulty_target) + str(self.nonce) + str(self.block_data)
            
            hashed_value = hashlib.sha256(str_to_hash.encode('utf-8')).hexdigest()
            
            if hashed_value[:self.difficulty_target] == "0" * self.difficulty_target:
                hash_is_valid = True
            else:
                self.nonce += 1

        
        return hashed_value