class BlockData:
    def __init__(self, data):
        self.data = data

    def input_data(self, owner, price, nft_art):
        self.data['owner'] = owner
        self.data['price'] = price
        self.data['nft_art'] = nft_art