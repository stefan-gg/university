import os
import cv2
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# load data from minst
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# reshape
X_train = X_train.reshape((X_train.shape[0], 28, 28, 1)).astype('float32')
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1)).astype('float32')
# normalizing inputs from 0-255 to 0-1
X_train = X_train / 255
X_test = X_test / 255

# converting the labels to binary class matrices.
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]

# create model
model = Sequential()
# when using this layer as the first layer we need to provide input_shape
model.add(Conv2D(30, (3, 3), input_shape=(28, 28, 1), activation='relu'))
# downsamples the input along its spatial dimensions (height and width)
# by taking the maximum value over an input window (of size defined by pool_size)
# for each channel of the input
model.add(MaxPooling2D())
#model.add(Conv2D(15, (5, 5), activation='relu'))
model.add(Conv2D(15, (3, 3), activation='relu'))
model.add(MaxPooling2D())
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=15, batch_size=200)

scores = model.evaluate(X_test, y_test, verbose=0)

model.save(r'models\\digits_model.h5')



# we can test the data from picures here if we uncomment the rest of the code below

# model = tf.keras.models.load_model('models\\digits_model.h5')
# # loading the images from the folder and predicting them.
# image_number = 0
# while os.path.isfile('C:/Users/Stefan/Desktop/git-uni/university/CS374-ArtificialInteligence/CS374-Project/images/characters/Character_{}.png'.format(image_number)):
#     try:
#         img = cv2.imread('C:/Users/Stefan/Desktop/git-uni/university/CS374-ArtificialInteligence/CS374-Project/images/characters/Character_{}.png'.format(image_number))[:,:,0]
#         img = cv2.resize(img, (28, 28))
#         img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]
#         img = np.invert(np.array([img]))
#         prediction = model.predict(img)
        
#         for n in prediction:
#             for element in n:
#                 if element == 1.0:
#                     print(element)
            
#         print("The number is probably a {}".format(np.argmax(prediction)))
#         print(prediction)
#         plt.imshow(img[0], cmap=plt.cm.binary)
#         plt.show()
#         image_number += 1
#     except:
#         print("Image with name : Character_" + str(image_number) + ".png is not found")
#         image_number += 1