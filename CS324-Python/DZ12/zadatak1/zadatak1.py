import numpy as np
import pandas as pd


niz1 = np.random.randint(5, 11, 500)
niz2 = np.random.randint(5, 11, 500)
niz3 = np.random.randint(5, 11, 500)
niz4 = np.random.randint(16, size=(500))
niz5 = np.random.randint(2, size=(500))
niz6 = np.random.randint(5, 11, 500)

for i in range(500):
    if (niz1[i] in range(8, 11) or niz3[i] in range(9, 11)) and niz6[i] < 10:
        niz6[i] += 1
    if niz4[i] in range(5, 13) and niz6[i] > 5:
        niz6[i] -= 1
    elif niz4[i] in range(13, 16) and niz6[i] > 6:
        niz6[i] -= 2
    if niz5[i] == 0:
        niz6[i] = 5

data = pd.DataFrame({"cs_101_ocena": niz1, "it_101_ocena": niz2, "ma_101_ocena": niz3,
                    "cs115_izostanci": niz4, "cs_115_polozen": niz5, "cs_115_ocena": niz6})

data.to_csv("dataset.csv", index=False)
