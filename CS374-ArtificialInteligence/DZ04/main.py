"""
Podeliti podatke na trening i test skup, izvršiti klasifikaciju
 pomoću k-NN algoritma i prikazati tačnost. 
Prikazati tačnost za različite vrednosti parametra k. 
Testirati za 3, 5, 7 i 9, a u slučaju da tačnost raste,
 možete probati i za veće vrednosti. Diskutovati rezultate. 
Pokrenuti težinsku varijantu (težine zavise od udaljenosti) 
i proveriti da li se tačnost menja i kako. 
Eksprimentisati sa nekom od sledećih tehnika po vašem izboru 
i prikazati kako se menja tačnost klasifikacije: 
Promena metrike rastojanja
"""

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("Social_Network_Ads.csv")
# podaci iz Gender kolone se pretvaraju u numeričke vrednosti
data = pd.get_dummies(data, columns=['Gender'], drop_first=True)

X = data.drop("Purchased", axis = 1)
y = data['Purchased']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.25, random_state = 100)

imena_kolona = X.columns

sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

X_train = pd.DataFrame(X_train, columns = imena_kolona)
X_test = pd.DataFrame(X_test, columns = imena_kolona)

k_vrednosti = [3, 5, 7, 9]

for n in k_vrednosti:

    knn = KNeighborsClassifier(n_neighbors = n,metric = 'minkowski', p=2)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    preciznost = accuracy_score(y_pred, y_test)
    print("Preciznost za k = " + str(n) + " je -> " + str(preciznost))

    # metrika rastojanja je dodata
    knn = KNeighborsClassifier(n_neighbors = n,metric = 'minkowski', p=2, weights='distance')
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    preciznost = accuracy_score(y_pred, y_test)
    print("Preciznost sa dodatom metrikom rastojanja za k = " + str(n) + " je -> " + str(preciznost))

    # promenjena je metrika rastojanja - chebyshev
    knn = KNeighborsClassifier(n_neighbors = n, metric = 'chebyshev', p=2)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    preciznost = accuracy_score(y_pred, y_test)
    print("Preciznost (sa chebyshev metrikom rastojanja) za k = " + str(n) + " je -> " + str(preciznost) + "\n")
