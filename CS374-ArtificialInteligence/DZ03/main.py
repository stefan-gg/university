import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import rand
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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


min_len = min(len(X_train), len(y_train))
# Fitting a linear regression model to the data.
regressor = LinearRegression()
regressor.fit(X_train[0:min_len], y_train[0:min_len])
print("**********************")
print(regressor.intercept_)
print(regressor.coef_)
print("**********************")
y_pred = regressor.predict(X_test)
print(y_test)
print("********")
print(y_pred)
print("********")
min_len = min(len(y_pred), len(y_train))
df = pd.DataFrame({'Actual':y_test[0:min_len], 'Predicted': y_pred[0:min_len]})
print(df)

#plt.scatter(y_pred[0:min_len], y_test[0:min_len])
#plt.title('y_test vs y_pred')
#plt.xlabel('y_pred')
#plt.ylabel('y_test')
#plt.show()

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

# plt.scatter(y_pred, y_test)
# plt.title('y_test vs y_pred')
# plt.xlabel('y_pred')
# plt.ylabel('y_test')
# plt.show()