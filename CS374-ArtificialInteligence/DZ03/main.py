import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import rand
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import math

dataset = pd.read_csv("Life_Expectancy_Data.csv")
gdp = dataset[['GDP']]
life_expectancy = dataset['Life expectancy']

plt.scatter(gdp, life_expectancy)
plt.title('GDP vs Life expectancy')
plt.xlabel('GDP')
plt.ylabel('Life expectancy')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(gdp, life_expectancy, test_size=0.2, random_state=0)

# Replacing the infinite values with NaN and then dropping the NaN values.
# Zbog pojavljivanja NaN vrednosti sam morao da dodam kod ispod
# Takođe sam posle ovog zadatka odradio još jedan primer na kojem su brojke normalnije ispale
X_train.replace([np.inf, -np.inf], np.nan, inplace=True)
X_train.dropna(inplace=True)

X_test.replace([np.inf, -np.inf], np.nan, inplace=True)
X_test.dropna(inplace=True)

y_train.replace([np.inf, -np.inf], np.nan, inplace=True)
y_train.dropna(inplace=True)

# pošto sam morao da izbacujem elemente dužine nisu iste
# i zbog toga se min_len određuje više puta u ovom zadatku
min_len = min(len(X_train), len(y_train))
# Fitting a linear regression model to the data.
regressor = LinearRegression()
regressor.fit(X_train[0:min_len], y_train[0:min_len])
# print("**********************")
# print(regressor.intercept_)
# print(regressor.coef_)
# print("**********************")
y_pred = regressor.predict(X_test)

# Printing the actual values of y_test and the predicted values of y_pred.
# print(y_test)
# print("********")
# print(y_pred)
# print("********")


min_len = min(len(y_pred), len(y_train))

# iz nekog razloga se pojavljivala greška opet i nisam uspeo da rešim
# problem pa sam zbog toga uradio ovo sve to za primer ispod
#print('Mean absolute error: ', metrics.mean_absolute_error(y_test[0:min_len], y_pred[0:min_len]))
#print('Mean squared error: ', metrics.mean_squared_error(y_test[0:min_len], y_pred[0:min_len]))
#print('Root mean squared error: ', metrics.mean_squared_error(y_test[0:min_len], y_pred[0:min_len]))


df = pd.DataFrame({'Actual':y_test[0:min_len], 'Predicted': y_pred[0:min_len]})
print(df)

plt.scatter(gdp[0:min_len], y_pred[0:min_len])
plt.title('y_pred & gdp')
plt.ylabel('y_pred')
plt.xlabel('gdp')
plt.show()

plt.scatter(gdp[0:min_len], y_test[0:min_len])
plt.title('y_test & gdp')
plt.ylabel('y_test')
plt.xlabel('gdp')
plt.show()

# Drugi primer *****************************

# dataset = pd.read_csv("scores.csv")
# X = dataset[["Hours"]]
# y = dataset["Scores"]

# plt.scatter(X, y)
# plt.title('X vs Y')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# regressor = LinearRegression()
# regressor.fit(X_train, y_train)

# print(regressor.intercept_)
# print(regressor.coef_)

# y_pred = regressor.predict(X_test)
# df = pd.DataFrame({'Actual':y_test, 'Predicted': y_pred})
# print(df)

# print('Mean absolute error:', metrics.mean_absolute_error(y_test, y_pred))
# print('Mean squared error:', metrics.mean_squared_error(y_test, y_pred))
# print('Root mean squared error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# plt.scatter(y_pred, y_test)
# plt.title('y_test vs y_pred')
# plt.xlabel('y_pred')
# plt.ylabel('y_test')
# plt.show()