import pandas as pd
import time
import csv
import math

imena_polja = ["iteracija", "y(x)", "g(x)"]

with open("zadatak1/trig.csv", "w", newline="") as rezultati:
    upis_u_fajl = csv.DictWriter(rezultati, fieldnames=imena_polja)
    upis_u_fajl.writeheader()

for broj in range(1, 60):
    with open("zadatak1/trig.csv", "a", newline="") as rezultati:
        upis_u_fajl = csv.DictWriter(rezultati, fieldnames=imena_polja)

        y = math.sin(broj) - 3
        g = math.cos(broj) + 3

        podaci = {"iteracija": broj, "y(x)": y, "g(x)": g}

        upis_u_fajl.writerow(podaci)

    time.sleep(1)
