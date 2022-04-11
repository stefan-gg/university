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