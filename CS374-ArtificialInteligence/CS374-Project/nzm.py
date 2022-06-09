import cv2
import numpy
import numpy as np
from PIL import Image
image = cv2.imread('C:\\Users\\Stefan\Desktop\\ai\\Character_6.png')
image = numpy.invert(image)
image = numpy.invert(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', image)
#bez gray vrv
cv2.imshow('a', gray)
#img = np.invert(Image.open("Character_0.png").convert('L')).ravel()
#cv2.imshow('aa', img)
cv2.waitKey()