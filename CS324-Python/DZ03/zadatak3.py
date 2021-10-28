import random

brojevi = {}
broj_generisanja = 4056 // 3
broj_elementa = 4056 % 3

for broj in range(broj_generisanja):
    rand_broj = random.uniform(40, 56)
    brojevi.update({broj : rand_broj})

print("%.3f" % (brojevi.get(broj_elementa)))

""" for broj, vrednost in brojevi.items():
    if(broj < broj_elementa):
        print(broj, vrednost) """