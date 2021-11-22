import re

broj_indeksa = 4056
pattern = re.compile(r"(?m)^[0-9]{3}\s{1}.*")
podatak = ""

with open("zadatak1/podaci.txt", 'r') as podaci:
    podatak = podaci.read()

rezultati = pattern.finditer(podatak)

with open("zadatak1/adrese.txt", 'w') as upis:
    for rezultat in rezultati:
        if str(broj_indeksa % 10) == rezultat.group(0)[0]:
            upis.write(rezultat.group(0) + "\n")
