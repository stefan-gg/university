import numpy as np

parne_matrice = [0, 2, 4, 6, 8]
neparne_matrice = [1, 3, 5, 7, 9]

np.random.seed(7)

niz = np.random.randint(-50, 50, (10, 10, 10))

#print(niz)

#0 2 4 6 8 matrica
print("Parne matrice")
for broj in parne_matrice:
    print("Matrica broj " + str(broj + 1))
    print(niz[broj, ..., :])

#prvi redovi neparnih matrica
print("Neparne matrice")
for broj in neparne_matrice:
    print("Matrica broj " + str(broj + 1))
    print(niz[broj, 0, :])

#1. do 8. reda 7 8 9 matrice
print("Od prvog do osmog reda 7, 8 i 9 matrice")
print(niz[7, 0, 0:9])
print(niz[8, 0, 0:9])
print(niz[9, 0, 0:9])

#svi redovi poslednje matrice
print("Svi redovi poslednje matrice")
print(niz[-1, ..., :])

#5. 6. 7. element 4. reda pretposlednje matrice
print("5. 6. 7. element 4. reda pretposlednje matrice")
print(niz[-2, 3, 4:7])
