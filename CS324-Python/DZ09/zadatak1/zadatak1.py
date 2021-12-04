"""
Napisati program koji će za svaki položeni ispit računati prosečnu ocenu:

Sa tastature se unosi ocena (ne sme biti manja od 6) sve dok se ne pritisne ENTER.
Prilikom svakog unosa računa se prosečna ocena za (do tada) unete ocene.

Prvi grafikon štampa prosečna ocenu: iscrtava promenu prolazne ocene sa brojem položenih ispita.

Drugi grafikon štampa broj pojedinačnih ocena u pie grafikonu.
"""

from matplotlib import pyplot as plt
from collections import Counter

unete_ocene = []
prosek_ocena = []
prolazne_ocene = [6, 7, 8, 9, 10]


def srednjeVrednosti():
    suma = 0
    for ocena in unete_ocene:
        suma += ocena

    prosek_ocena.append(suma / len(unete_ocene))


while True:
    ocena = int(
        input("Unesite ocenu dobijenu na ispitu (mora da bude veća od 5 i manja od 11)"))
    if ocena in prolazne_ocene:
        unete_ocene.append(ocena)
        srednjeVrednosti()
        print(f"Prosek za sada iznosi {prosek_ocena[len(prosek_ocena) - 1]}")
    else:
        break

# graph
plt.plot(range(1, len(unete_ocene) + 1), unete_ocene, 'o', label='Ocene')
plt.plot(range(1, len(unete_ocene) + 1),
         prosek_ocena, '>--', label='Prosek ocena')
plt.xlabel("Prosek")
plt.ylabel("Ocene")
plt.xlabel("Broj položenih ispita")

plt.legend()
plt.show()


# pie
ocene_pie = []
broj_ocena = []
brojanje_ocena = Counter(unete_ocene)
print(brojanje_ocena)
print(ocene_pie)
print(broj_ocena)
for ocene, broj in brojanje_ocena.items():
    ocene_pie.append(ocene)
    broj_ocena.append(broj)

plt.pie(broj_ocena, labels=ocene_pie, autopct="%.1f%%", startangle=60, wedgeprops={"edgecolor": "white", "linewidth": 2})
plt.title("Broj pojedinačnih ocena")
plt.show()