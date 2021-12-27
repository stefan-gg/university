"""
Istrenirati model linearna regresije da estimira vrednosti kolone cs_115_ocena, ako su ulazni podaci:

Samo kolona cs_101 ocena,
Samo kolona cs_115_izostanci,
Sve kolone (osim cs_115_ocena i cs_115_polozen, naravno)
Istrenirati modele linearne regresije (koristiti 75%, a zatim 90% 
skupa za trening skup) za svaku od traženih kolona, naći broj grešaka
i tačnost za svaki, i zaključiti koji je model najbolje koristiti. 
Kada se koristi samo jedna kolona,
nacrtati i grafike estimiranih vrednosti naspram pravih vrednosti.
"""
from os import error
import numpy as np
import pandas as pd
from matplotlib import colors, pyplot as plt
import sklearn
from sklearn import linear_model


def prikazEstimiranihVrednosti(x, y, procenat, ime_kolone):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
        x, y, train_size=procenat)
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train)

    predictions = linear.predict(x_test)

    novi_podaci = pd.DataFrame(x_test, columns=[ime_kolone])
    novi_podaci['Y'] = y_test
    novi_podaci['Prediction'] = predictions

    accuracy = linear.score(x_test, y_test)
    print(accuracy)

    plt.scatter(novi_podaci[ime_kolone], y_test, color='red')
    plt.plot(novi_podaci[ime_kolone], predictions, color='blue')
    plt.show()


podaci = pd.read_csv("dataset.csv")
praceni_podaci = ["cs_101_ocena", "cs_115_ocena"]
podaci_izvuceni = podaci[praceni_podaci]
predvidjanje = "cs_115_ocena"

# 1. deo
x = np.array(podaci_izvuceni.drop([predvidjanje], 1))
y = np.array(podaci[predvidjanje])

prikazEstimiranihVrednosti(x, y, 0.75, "cs_101_ocena")
prikazEstimiranihVrednosti(x, y, 0.90, "cs_101_ocena")

# 2. deo
praceni_podaci = ["cs115_izostanci", "cs_115_ocena"]
podaci_izvuceni = podaci[praceni_podaci]
predvidjanje = "cs_115_ocena"

x = np.array(podaci_izvuceni.drop([predvidjanje], 1))
y = np.array(podaci[predvidjanje])

prikazEstimiranihVrednosti(x, y, 0.75, "cs115_izostanci")
prikazEstimiranihVrednosti(x, y, 0.90, "cs115_izostanci")

# 3. deo
praceni_podaci = ["cs_101_ocena", "it_101_ocena",
                  "ma_101_ocena", "cs115_izostanci", "cs_115_ocena"]
podaci_izvuceni = podaci[praceni_podaci]
predvidjanje = "cs_115_ocena"

x = np.array(podaci_izvuceni.drop([predvidjanje], 1))
y = np.array(podaci[predvidjanje])
# 75%
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    x, y, train_size=0.75)
linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)

predictions = linear.predict(x_test)
accuracy = linear.score(x_test, y_test)
errors = np.sum(np.where(y_test != predictions))
print(accuracy, " ",errors)
# 90%
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    x, y, train_size=0.90)
linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)

predictions = linear.predict(x_test)
accuracy = linear.score(x_test, y_test)
errors = np.sum(np.where(y_test != predictions))
print(accuracy, " ", errors)
