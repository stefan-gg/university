import matplotlib.pyplot as plt
import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Dropout
from keras.optimizers import SGD, Adam
from keras.callbacks import ReduceLROnPlateau, EarlyStopping
from keras.utils import to_categorical
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import tensorflow as tf
import os

path = os.getcwd()
data = pd.read_csv(path + "\letters\A_Z Handwritten Data\A_Z_Handwritten_Data.csv").astype('float32')

X = data.drop('0',axis = 1)
y = data['0']

train_x, test_x, train_y, test_y = train_test_split(X, y, test_size = 0.2)
train_x = np.reshape(train_x.values, (train_x.shape[0], 28,28))
test_x = np.reshape(test_x.values, (test_x.shape[0], 28,28))

print("Train data shape: ", train_x.shape)
print("Test data shape: ", test_x.shape)

word_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X', 24:'Y',25:'Z'}


train_X = train_x.reshape(train_x.shape[0],train_x.shape[1],train_x.shape[2], 1)
print("New shape of train data : ", train_X.shape)
test_X = test_x.reshape(test_x.shape[0], test_x.shape[1], test_x.shape[2], 1)
print("New shape of train data : ", test_X.shape)

train_yOHE = to_categorical(train_y, num_classes = 26, dtype='int')
print("New shape of train labels : ", train_yOHE.shape)
test_yOHE = to_categorical(test_y, num_classes = 26, dtype='int')
print("New shape of test labels : ", test_yOHE.shape)

model = Sequential()
model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)))
model.add(MaxPool2D(pool_size=(2, 2), strides=2))
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu', padding = 'same'))
model.add(MaxPool2D(pool_size=(2, 2), strides=2))
model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu', padding = 'valid'))
model.add(MaxPool2D(pool_size=(2, 2), strides=2))
model.add(Flatten())
model.add(Dense(64,activation ="relu"))
model.add(Dense(128,activation ="relu"))
model.add(Dense(26,activation ="softmax"))

model.compile(optimizer = Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(train_X, train_yOHE, epochs=5,  validation_data = (test_X,test_yOHE))

model.summary()
model.save(r'models\letters_model.h5')

print("The validation accuracy is :", history.history['val_accuracy'])
print("The training loss is :", history.history['loss'])
print("The validation loss is :", history.history['val_loss'])
print("The training accuracy is :", history.history['accuracy'])



# we can test the data from picures here if we uncomment the rest of the code below
# word_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X', 24:'Y',25:'Z'}

# model = tf.keras.models.load_model('models\\letters_model.h5')

# img = cv2.imread(r'C:\\Users\\Stefan\\Desktop\\git-uni\\university\\CS374-ArtificialInteligence\\CS374-Project\\images\\characters\\Character_1.png')
# img_copy = img.copy()
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img = cv2.resize(img, (400,440))

# img_copy = cv2.GaussianBlur(img_copy, (7,7), 0)
# img_gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
# _, img_thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)
# img_final = cv2.resize(img_thresh, (28,28))
# img_final = np.reshape(img_final, (1,28,28,1))


# img_pred = word_dict[np.argmax(model.predict(img_final))]
# print(word_dict[np.argmax(model.predict(img_final))])
# print(model.predict(img_final))

# print("Prediction is + " + img_pred)