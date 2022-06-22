import cv2
from imutils import contours
import numpy as np
import os
from pytesseract import pytesseract
from PIL import Image
import matplotlib.pyplot as plt
import tensorflow as tf

from sympy import symbols
from sympy import sympify, solve, Eq
import py_expression_eval

def get_text_from_image():
        # getting path oh the current working directory
        image_name = input("Type image name (with the extension) >>")
        path = os.getcwd()
        image = cv2.imread(path + '/images/equations/' + image_name)
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
                cv2.imwrite('images\characters\Character_{}.png'.format(ROI_number), ROI)

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

        path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        #image_name = input("Input name of image (and the image extension also) >>")

        img = Image.open(path + '/images/equations/' + image_name) #+ image_name)

        pytesseract.tesseract_cmd = path_to_tesseract

        text = pytesseract.image_to_string(img)

        text_from_image = ""
        predicition = ""
        operations = ["*", "+", "=", "/", "."]

        for l in text:
                if l.isalpha() or l.isdigit() or l in operations:
                        text_from_image += l
        text_from_image = text_from_image.replace("=", "==")

        print("Tesseract found : " + text_from_image)
        
        for i in range(0, ROI_number):
                # tesseract is not recognizing minus so i had to manualy recognize it
                width, height = Image.open(path + '/images/characters/Character_{}.png'.format(i)).size
                num_of_pixels = width*height

                image_ = cv2.imread(path + '/images/characters/Character_{}.png'.format(i), 0)
                count = cv2.countNonZero(image_)


                if count <= int(num_of_pixels * 0.2):
                        if text_from_image[i] != "=":
                                text_from_image = text_from_image[0:i] + "-" + text_from_image[i:]

                if text_from_image[i].isalpha():

                        model = tf.keras.models.load_model('models\letters_model.h5')

                        word_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X', 24:'Y',25:'Z'}

                        img = cv2.imread(path + '/images/characters/Character_{}.png'.format(i))
                        img_copy = img.copy()
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        img = cv2.resize(img, (400,440))

                        img_copy = cv2.GaussianBlur(img_copy, (7,7), 0)
                        img_gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
                        _, img_thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)
                        img_final = cv2.resize(img_thresh, (28,28))
                        img_final = np.reshape(img_final, (1,28,28,1))

                        img_pred = word_dict[np.argmax(model.predict(img_final))]

                        predicition += img_pred
                        print("i ->>>>>>>>>" + str(i))
                elif text_from_image[i].isdigit():

                        model = tf.keras.models.load_model('models\digits_model.h5')

                        try:
                                img = cv2.imread(path + '/images/characters/Character_{}.png'.format(i))[:,:,0]
                                img = cv2.resize(img, (28, 28))
                                img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]
                                img = np.invert(np.array([img]))
                                prediction = model.predict(img)

                                print("The number is probably a {}".format(np.argmax(prediction)))
                                print(prediction)
                                predicition += str(np.argmax(prediction))
                        except:
                            print("Image with name : Character_" + str(i) + ".png is not found")
        
                else:
                        predicition += text_from_image[i]

        print(predicition.replace("==", "="))
        return predicition.replace("==", "=")



equation_1 = get_text_from_image()
equation_2 = get_text_from_image()

parser = py_expression_eval.Parser()

exp_1 = parser.parse(equation_1.split("=")[0])
print(exp_1.variables()[0])

exp_2 = parser.parse(equation_2.split("=")[0])
print(exp_2.variables()[0])

variables = ""

for index in range(len(exp_1.variables())):
        if not exp_2.variables()[index] in variables:
                variables += exp_2.variables()[index] + " "   

for index in range(len(exp_1.variables())):
        if not exp_2.variables()[index] in variables:
                variables += exp_2.variables()[index] + " "  

variables = variables[:-1]

if len(variables) > 3:
        print("There are too many variables for this program to solve !")

else:
        try:
            expr = Eq(sympify(equation_1.split("=")[0], evaluate=False), sympify(equation_1.split("=")[1], evaluate=False))
            expr2 = Eq(sympify(equation_2.split("=")[0], evaluate=False), sympify(equation_2.split("=")[1], evaluate=False))
            x, y = symbols(variables)
            solution = solve((expr, expr2),(x, y))
            print("Solutions are : " + str(solution[x]) + str(solution[y]))
        except:
            print("No solution were found for the equations.")