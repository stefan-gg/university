from asyncio.windows_events import NULL
import os
from PIL import Image
from block import Block
from nft_art import NFTArt
from block_data import BlockData
from block_header import BlockHeader
from transaction import Transaction
from block import Block
import time
import io
import PySimpleGUI as sg
import re

def loadImages(path):
    imagesList = os.listdir(path)
    loadedImages = []
    for image in imagesList:
        img = Image.open(path + image)
        loadedImages.append(img)
    return loadedImages

#path = './images/'
path = "C:/Users/Stefan/Desktop/git-uni/university/IT475-Blockchain/projekat/nft/nft-structure/images/"

images = loadImages(path)
owners = ['stefan', 'jovan', 'marko']
prices = ['3 ETH', '6.2 ETH', '4.3 ETH']
buyers = ['john', 'jack', 'bob']

counter = 0

blockchain = []

# Loading the images from the folder and adding them to the blockchain.
for img in images:
    art = NFTArt(img)
    b_data = BlockData()
    b_data.input_data(owners[counter], prices[counter], art)
    prev_hash = 0
    if len(blockchain) != 0:
        prev_hash = blockchain[counter - 1].block_header.block_hash
    b_header = BlockHeader(prev_hash, 2, 0, b_data)
    transaction = NULL
    block = Block(b_header, transaction)

    blockchain.append(block)

    time.sleep(1)
    counter += 1

for block in blockchain:
    print(block, end='\n\n')

layout = [
    [sg.Image(key="-IMAGE-")],
    [
        sg.Button("Load images"),
        sg.Button("Previous"),
        sg.Button("Next")
    ],
    [sg.Text('Price of this NFT is: ', key="-PRICE-")],
    [
        [sg.Text('Name', size =(7, 0)), sg.InputText()],
        [sg.Text('Amount', size =(7, 0)), sg.InputText()],
        [sg.Submit("Submit")]
    ]
]

win = sg.Window("NFT blockchain", layout)

img_index = 0

while True:
    event, values = win.read()
    win["-PRICE-"].update('Price of this NFT is: ')
    if event == sg.WIN_CLOSED:
        break
    if event == "Previous":
        if img_index == 0:
            img_index = len(images) - 1
        else:
            img_index -= 1
    elif event == "Next":
        if img_index == len(images) - 1:
            img_index = 0
        else:
            img_index += 1

    img = images[img_index]
    img.thumbnail((400, 400))
    bio = io.BytesIO()
    img.save(bio, format="PNG")

    win["-IMAGE-"].update(data=bio.getvalue())
    price = '0 ETH'
    for block in blockchain:
        if block.block_header.block_data.data["nft_art"].nft_image == images[img_index]:
            price = block.block_header.block_data.data["price"]
            break
    win["-PRICE-"].update(win["-PRICE-"].get() + price)

    flag = False

    if event == "Submit":
        if values[0] != '' and values[1] != '':
            NFTPrice = price.replace(" ETH", "")
            for i in values[1]:
                if i not in '0123456789':
                    sg.Popup('The amount needs to be inputed as number that represents value in ETH.', keep_on_top=True)
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                if float(NFTPrice) <= float(values[1]):
                    
                    #TODO: Napisati da se kupi nft i upis u blockchain
                    
                    name = values[0]
                    amount = values[1]
                    image_name = images[img_index]
                    
                    for block in blockchain:
                        if block.block_header.block_data.data["nft_art"].nft_image == images[img_index]:
                            art = NFTArt(image_name)
                            b_data = BlockData()
                            b_data.input_data(name, amount, art)
                            
                            prev_hash = blockchain[len(blockchain) - 1].block_header.block_hash
                            b_header = BlockHeader(prev_hash, 2, 0, b_data)

                            transaction = NULL

                            block = Block(b_header, transaction)
                            blockchain.append(block)

                        for block in blockchain:
                            print(block)
                            print(" ")
                        break
                else:
                    sg.Popup("Inputed amout is less then required amount.", keep_on_top=True)
        else:
            sg.Popup("Please input values in all fields.", keep_on_top=True)


win.close()