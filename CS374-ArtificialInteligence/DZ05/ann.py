from tensorflow import keras
from keras.models import Sequential
from keras.layers import Flatten
from keras.layers import Dense

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train_norm = x_train / 255
x_test_norm = x_test / 255

x_validation, x_train = x_train_norm[:5500], x_train_norm[5500:]
y_validation, y_train = y_train[:5500], y_train[5500:]

x_test = x_test_norm

model = Sequential()
model.add(Flatten(input_shape=[28, 28]))
model.add(Dense(350, activation="relu"))
model.add(Dense(140, activation="relu"))
model.add(Dense(10, activation="softmax"))

model.summary()

model.compile(loss="sparse_categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])

model.fit(x_train, y_train, epochs=15)

model.evaluate(x_test, y_test)