import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
import numpy as np


podaci = pd.read_csv("Student_izvestaj.csv")

prebrojani_podaci = Counter(podaci["Ocena"])

ocene = []
broj_ocena = []
srednje_ocene = []
figura = plt.figure()
brojac = 0
suma = 0

for broj in podaci["Ocena"]:
    suma += broj
    brojac += 1
    srednje_ocene.append(suma / brojac)

predmeti = podaci["Predmet"].copy()
for predmet in range(len(predmeti)):
    predmeti[predmet] = predmeti[predmet][:2]

brojac_ocena = Counter(predmeti)

# pie graph
for ocena, broj in prebrojani_podaci.items():
    broj_ocena.append(broj)
    ocene.append(ocena)

figura_1 = figura.add_subplot(2, 2, 1)
figura_1.pie(broj_ocena, labels=ocene, autopct="%.1f%%",
             startangle=60, wedgeprops={"edgecolor": "white", "linewidth": 2})

# horizontalni graph
figura_2 = figura.add_subplot(2, 2, 2)
plt.barh(list(brojac_ocena.keys()), list(brojac_ocena.values()))
plt.ylabel("Ocena")
plt.xlabel("Broj ocena")

# linijski plot
figura_3 = figura.add_subplot(2, 2, (3, 4))
plt.plot(range(len(podaci["Ocena"])), srednje_ocene, "g-", label="Prosek")
plt.plot(range(len(podaci["Ocena"])), podaci["Ocena"], "ro", label="Ocena")

plt.savefig("slika/student_izvestaj.png")
plt.show()
