from nft_art import NFTArt

class BlockData:
    def __init__(self):
        self.data = {}

    # dictionary
    def input_data(self, owner, price, nft_art: NFTArt):
        self.data['owner'] = owner
        self.data['price'] = price
        self.data['nft_art'] = nft_art

    def __str__(self):
        return self.data['owner'] + " " + self.data['price'] + str(self.data['nft_art'])