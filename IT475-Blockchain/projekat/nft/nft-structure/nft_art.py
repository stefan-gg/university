import hashlib

class NFTArt:
    def __init__(self, nft_name, nft_id):
        self.nft_name = nft_name
        self.nft_id = nft_id
    
    #TODO id = hash ime_slike + ...
    def hash_nft_data(self, block_data):
        string_to_hash = self.nft_name + self.nft_id + block_data
        hashed_value = hashlib.sha256(string_to_hash.encode('utf-8')).hexdigest()
        return hashed_value