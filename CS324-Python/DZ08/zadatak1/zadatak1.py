import numpy as np

# Korišćenjem numpy paketa napraviti sledeće matrice. Nije dozvoljen ručni unos vrednosti po
# indeksu, već treba uneti matricu u matricu.

#prva matrica
prva_matrica = np.identity(3);

print("Prva matrica")
print(prva_matrica)

#druga matrica
druga_matrica = np.zeros((4, 2))
sredisnja_matrica = np.full((2,2), 0)

sredisnja_matrica = np.insert(sredisnja_matrica, 1, 10, 1)
sredisnja_matrica = np.insert(sredisnja_matrica, 1, 10, 1)

druga_matrica = np.insert(druga_matrica, 1, sredisnja_matrica, 1)

print("Druga matrica")
print(druga_matrica)

#treca matrica
treca_matrica = np.ones((2, 3))
sredisnja_matrica = np.zeros((3, 2))
sredisnja_matrica = np.insert(sredisnja_matrica, 1, [0, 1, 0], 1)

treca_matrica = np.insert(treca_matrica, 1, sredisnja_matrica, 0)

#napravio sam ovu matricu kako bih mogao da je dodam na početak i kraj prethodne matrice
matrica_jedinice = np.ones((1,5));

treca_matrica = np.insert(treca_matrica, 0, matrica_jedinice, 1)
treca_matrica = np.insert(treca_matrica, 4, matrica_jedinice, 1)

print("Treća matrica")
print(treca_matrica)