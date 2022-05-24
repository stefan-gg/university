from datetime import datetime

class Transaction:
    def __init__(self, seller, buyer, price, nft_art, gas_fee, wei_fee):
        self.seller = seller
        self.buyer = buyer
        self.price = price
        self.nft_art = nft_art
        self.gas_fee = gas_fee
        self.wei_fee = wei_fee
        self.timestamp = datetime.now()
    
    def __str__(self):
        return "Seller: " + self.seller + ", Buyer: " + self.buyer + ", Price: " + self.price + ", NFT art: " + self.nft_art + ", Gas fee: " + self.gas_fee + ", Wei: " + self.wei_fee + ", Timestamp: " + self.timestamp