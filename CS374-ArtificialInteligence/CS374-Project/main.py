import cv2
from imutils import contours

image = cv2.imread('C:\\Users\\Stefan\\Desktop\\git-uni\\university\\CS374-ArtificialInteligence\\CS374-Project\\images\\equations\\ajde.jpg')
# Converting the image to grayscale.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray image", gray)

# Pixels values are either 0 or 255
# Thresholding is the binarization of an image
# Otsu's threshold attempts to be more dinamic and automatically compute optimal treshold
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]

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
        x,y,w,h = cv2.boundingRect(c)

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

#cv2.imshow('thresh', thresh)
cv2.imshow('image', image)
cv2.waitKey()
