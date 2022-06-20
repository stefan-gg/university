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

# load data
# (X_train, y_train), (X_test, y_test) = mnist.load_data()
# # reshape to be [samples][width][height][channels]
# X_train = X_train.reshape((X_train.shape[0], 28, 28, 1)).astype('float32')
# X_test = X_test.reshape((X_test.shape[0], 28, 28, 1)).astype('float32')
# # normalize inputs from 0-255 to 0-1
# X_train = X_train / 255
# X_test = X_test / 255

# # converting the labels to binary class matrices.
# y_train = np_utils.to_categorical(y_train)
# y_test = np_utils.to_categorical(y_test)
# num_classes = y_test.shape[1]

#drugi model************************************************
# model = Sequential()
# model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=input_shape))
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.25))
# model.add(Flatten())
# model.add(Dense(256, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(num_classes, activation='softmax'))
#drugi model************************************************

# # create model
# model = Sequential()
# # when using this layer as the first layer we need to provide input_shape
# model.add(Conv2D(30, (5, 5), input_shape=(28, 28, 1), activation='relu'))
# model.add(MaxPooling2D())
# model.add(Conv2D(15, (3, 3), activation='relu'))
# model.add(MaxPooling2D())
# model.add(Dropout(0.2))
# model.add(Flatten())
# model.add(Dense(128, activation='relu'))
# model.add(Dense(50, activation='relu'))
# model.add(Dense(num_classes, activation='softmax'))

# # compile model
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# # fit the model
# model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=200)
# # final evaluation of the model
# scores = model.evaluate(X_test, y_test, verbose=0)
# # saving the model
# model.save(r'models\\digits_model.h5')
model = tf.keras.models.load_model('models\\digits_model.h5')
# loading the images from the folder and predicting them.
image_number = 0
while os.path.isfile('C:/Users/Stefan/Desktop/git-uni/university/CS374-ArtificialInteligence/CS374-Project/images/characters/Character_{}.png'.format(image_number)):
    try:
        img = cv2.imread('C:/Users/Stefan/Desktop/git-uni/university/CS374-ArtificialInteligence/CS374-Project/images/characters/Character_{}.png'.format(image_number))[:,:,0]
        img = cv2.resize(img, (28, 28))
        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]
        img = np.invert(np.array([img]))
        prediction = model.predict(img)
        
        for n in prediction:
            for element in n:
                if element == 1.0:
                    print(element)
            
        print("The number is probably a {}".format(np.argmax(prediction)))
        print(prediction)
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
        image_number += 1
    except:
        print("Image with name : Character_" + str(image_number) + ".png is not found")
        image_number += 1