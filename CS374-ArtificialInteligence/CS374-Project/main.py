import cv2
from imutils import contours
import numpy as np
import os
from pytesseract import pytesseract
from PIL import Image
import matplotlib.pyplot as plt

# getting path oh the current working directory
path = os.getcwd()
image = cv2.imread(path + '/images/equations/eq.jpg')
# Converting the image to grayscale.
image = np.invert(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray image", gray)

# Pixels values are either 0 or 255
# Thresholding is the binarization of an image
# Otsu's threshold attempts to be more dinamic and automatically compute optimal treshold
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
cv2.imshow('image', thresh)
# Find contours, sort from left-to-right
# findContours() works best on binary images
# cv2.RETR_EXTERNAL retrieves only the extreme outer contours
# cv2.CHAIN_APPROX_SIMPLE compresses horizontal, vertical, and diagonal segments
#  and leaves only their end points
#  For example, an up-right rectangular contour is encoded with 4 points
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts, _ = contours.sort_contours(cnts, method="left-to-right")

# ROI = Region Of Interest
ROI_number = 0

for c in cnts:
    
    # Calculating the area of the contour.
    area = cv2.contourArea(c)

    if area > 10:

        # Drawing rectangle
        x, y, w, h = cv2.boundingRect(c)

        # Image array of values
        # 255 - values from array at y:y+h, x:x+w position
        ROI = 255 - image[y:y+h, x:x+w]

        # Saving the image in the current directory.
        # ROI is the array of values
        cv2.imwrite('images\\characters\\Character_{}.png'.format(ROI_number), ROI)

        # Drawing a rectangle around the image.
        # Parameters are :
        #  image
        #  start_point (tuple, x and y)
        #  end_point (tuple, but added width and height)
        #  color
        #  thickness
        cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
        
        ROI_number += 1



#image = cv2.resize(image, (400,440))
cv2.imshow('image', image)
cv2.waitKey()


image_number = 0
#while os.path.isfile(path + '/images/characters/Character_{}.png'.format(image_number)):
        
#converting image to text
        # image = Image.open(path + '/images/characters/Character_'+ str(image_number) +'.png')
        # print(pytesseract.image_to_string(image))

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  
        # Opening the image & storing it in an image object
img = Image.open(path + '/images/equations/eq.jpg')
img = np.invert(img)
        
pytesseract.tesseract_cmd = path_to_tesseract
        
text = pytesseract.image_to_string(img)
        
print(text[:-1])
oper = ["*", "+", "=", "/"]
for l in text:
        if l.isalpha() or l.isdigit() or l in oper:
                print(l)
image_number += 1
