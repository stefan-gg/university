from datetime import datetime
import hashlib

class BlockHeader:
    def __init__(self, previous_hash, difficulty_target: int, nonce: int, block_data):
        self.previous_hash = previous_hash
        self.timestamp = datetime.now()
        self.difficulty_target = difficulty_target
        self.nonce = nonce
        self.block_hash = self.set_block_hash()
        self.block_data = block_data

    #stara funkcija
    #def set_block_hash(self):
    #    str_to_hash = self.previous_hash + ' ' + str(self.timestamp) + ' ' + str(self.difficulty_target) + ' ' + str(self.nonce) + ' ' + str(self.block_data)
    #    hashed_value = hashlib.sha256(str_to_hash.encode('utf-8')).hexdigest()
    #    return hashed_value
    
    def validate_hash(self):

        hash = self.set_block_hash()

        if hash[:self.difficulty_target] == "0" * self.difficulty_target:
            return True
        else:
            return False

    #nova funkcija 
    def set_block_hash(self):
        #proof_of_work = 1
        hash_is_valid = False 
        hashed_value = ""

        while not hash_is_valid:
            #ostavio sam u 2 promenljive umesto u 1 da bi bilo manje prenatrpano
            #jer u 1 liniju da je nema se vidi sve lepo

            str_to_hash = self.previous_hash 
            + str(self.timestamp) 
            + str(self.difficulty_target)
            + str(self.nonce) + str(self.block_data)
            
            hashed_value = hashlib.sha256(str_to_hash.encode('utf-8')).hexdigest()
            
            if hashed_value[:self.difficulty_target] == "0" * self.difficulty_target:
                hash_is_valid = True
            else:
                self.nonce += 1

            return hashed_value