from os import listdir
from PIL import Image
from block import Block
from nft_art import NFTArt
from block_data import BlockData
from block_header import BlockHeader
from transaction import Transaction
from block import Block

def loadImages(path):
    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        img = Image.open(path + image)
        loadedImages.append(img)
    return loadedImages

path = './images/'

images = loadImages(path)
owners = ['stefan', 'jovan', 'marko']
prices = ['3 ETH', '6.2 ETH', '4.3 ETH']
buyers = ['john', 'jack', 'bob']

counter = 0

blockchain = []

for img in images:
    art = NFTArt(img)
    b_data = BlockData()
    b_data.input_data(owners[counter], prices[counter], art)
    prev_hash = 0
    if len(blockchain) != 0:
        prev_hash = blockchain[counter - 1].block_header.block_hash
    b_header = BlockHeader(prev_hash, 2, 0, b_data)
    transaction = Transaction(owners[counter], buyers[counter], prices[counter], art, 50, 100)
    block = Block(b_header, transaction)

    blockchain.append(block)
    counter += 1