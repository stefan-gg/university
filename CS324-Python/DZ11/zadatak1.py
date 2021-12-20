"""
1 Srednju vrednost trajanja studija na svim studijskim programima,
2 Srednju vrednost trajanja studija na pojedinačnim studijskim programima (BAS; MAS; DAS)
3 Najčešću vrednost trajanja studija po pojedinačnim studijskim programima,
4 Najčešću vrednost trajanja studija po univerzitetima,
5 Histogram broja studenata po trajanju studija, za naznačenom srednjom vrednošću,
6 Histogram broja studenata po univerzitetu
7 Pie grafikone raspodele studenata po studijskom programu, po univerzitetu
"""
from typing import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

podaci = pd.read_csv("data.csv")

trajanje, sp = podaci["Trajanje"], podaci["NivoStudija"]

# 1
print(round(np.mean(podaci["Trajanje"]), 3))

# 2
print(round(podaci.groupby(["NivoStudija"])["Trajanje"].mean(), 3))

# 3

print(podaci.groupby(["StudijskiProgram"])["Trajanje"].value_counts())

# 4
print(podaci.groupby(["Univerzitet"])["Trajanje"].value_counts())

# 5
trajanje_studija = podaci["Trajanje"].to_list()
sredina = np.mean(trajanje_studija)

plt.axvline(sredina, color="red")
plt.hist(trajanje_studija, edgecolor="black", linewidth=1.5)
plt.title("Histogram broja studenata po trajanju studija :")
plt.xlabel("Trajanje studija")
plt.ylabel("Broj studenata")

plt.show()

# 6
plt.hist(podaci["Univerzitet"].to_list(), edgecolor="green", linewidth=1.0)
plt.xticks(rotation=10)
plt.ylabel("Broj studenata")
plt.xlabel("Univerziteti")

plt.show()

# 7
raspored_po_studijskom_programu = Counter(podaci["StudijskiProgram"])

plt.pie(raspored_po_studijskom_programu.values(), labels=raspored_po_studijskom_programu.keys(
), startangle=40, autopct="%.1f%%", wedgeprops={"edgecolor": "white", "linewidth": 1})
plt.title("Raspodela studenata po studijskom programu")

plt.show()

raspored_po_univerzitetu = Counter(podaci["Univerzitet"])

plt.pie(raspored_po_univerzitetu.values(), labels=raspored_po_univerzitetu.keys(
), startangle=40, autopct="%.1f%%", wedgeprops={"edgecolor": "white", "linewidth": 1})
plt.title("Raspodela studenata po univerzitetu")

plt.show()