import hashlib
from datetime import datetime

class NFTArt:
    def __init__(self, nft_image):
        self.nft_image = nft_image
        self.token = self.generateToken()
    
    def generateToken(self):
        string_to_hash = self.nft_image.filename + str(self.nft_image.size) + self.nft_image.mode + self.nft_image.format
        return hashlib.sha256(string_to_hash.encode('utf-8')).hexdigest()

    def __str__(self):
        return "Token: " + self.token + ", Image: " + self.nft_image.filename.split('/')[2]