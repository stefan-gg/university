# import os
# import cv2
# import numpy as np
# import tensorflow as tf
# import matplotlib.pyplot as plt
# # Decide if to load an existing model or to train a new one
# train_new_model = False

# if train_new_model:
#     # Loading the MNIST data set with samples and splitting it
#     mnist = tf.keras.datasets.mnist
#     (X_train, y_train), (X_test, y_test) = mnist.load_data()

#     # Normalizing the data (making length = 1)
#     X_train = tf.keras.utils.normalize(X_train, axis=1)
#     X_test = tf.keras.utils.normalize(X_test, axis=1)

#     # Create a neural network model
#     # Add one flattened input layer for the pixels
#     # Add two dense hidden layers
#     # Add one dense output layer for the 10 digits
#     model = tf.keras.models.Sequential()
#     model.add(tf.keras.layers.Flatten())
#     model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
#     model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
#     model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

#     # Compiling and optimizing model
#     model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#     # Training the model
#     model.fit(X_train, y_train, epochs=3)

#     # Evaluating the model
#     val_loss, val_acc = model.evaluate(X_test, y_test)
#     print(val_loss)
#     print(val_acc)

#     # Saving the model
#     model.save('handwritten_digits.model')
# else:
#     # Load the model
#     model = tf.keras.models.load_model('handwritten_digits.model')

# # Load custom images and predict them
# image_number = 1
# while os.path.isfile('C:/Users/Stefan/Desktop/ai/Character_{}.png'.format(image_number)):
#     try:
#         img = cv2.imread('C:/Users/Stefan/Desktop/ai/Character_{}.png'.format(image_number))[:,:,0]
#         img = cv2.resize(img, (28, 28))
#         img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)[1]
#         img = np.invert(np.array([img]))
#         prediction = model.predict(img)
#         print("The number is probably a {}".format(np.argmax(prediction)))
#         print(prediction)
#         plt.imshow(img[0], cmap=plt.cm.binary)
#         plt.show()
#         image_number += 1
#     except:
#         print("Error reading image! Proceeding with next image...")
#         image_number += 1


# Larger CNN for the MNIST Dataset
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

# load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# reshape to be [samples][width][height][channels]
X_train = X_train.reshape((X_train.shape[0], 28, 28, 1)).astype('float32')
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1)).astype('float32')
# normalize inputs from 0-255 to 0-1
X_train = X_train / 255
X_test = X_test / 255

# Converting the labels to binary class matrices.
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]
# define the larger model
def larger_model():
	# create model
	model = Sequential()
	model.add(Conv2D(30, (5, 5), input_shape=(28, 28, 1), activation='relu'))
	model.add(MaxPooling2D())
	model.add(Conv2D(15, (3, 3), activation='relu'))
	model.add(MaxPooling2D())
	model.add(Dropout(0.2))
	model.add(Flatten())
	model.add(Dense(128, activation='relu'))
	model.add(Dense(50, activation='relu'))
	model.add(Dense(num_classes, activation='softmax'))
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model
# build the model
model = larger_model()
# Fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=200)
# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
# Saving the model
model.save(r'digits_model.h5')

# Loading the images from the folder and predicting them.
image_number = 1
while os.path.isfile('C:/Users/Stefan/Desktop/ai/Character_{}.png'.format(image_number)):
    try:
        img = cv2.imread('C:/Users/Stefan/Desktop/ai/Character_{}.png'.format(image_number))[:,:,0]
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
        print("Error reading image! Proceeding with next image...")
        image_number += 1