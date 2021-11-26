"""
Napraviti bazu podataka "biblioteka.db", koja sadrži tabelu:
knjige:

(katBroj int, naslov text, izdavac text, godinaIzdavanja int, izdata bool)

Napraviti funkciju za ubacivanja novih knjiga sa konzole. Ubacuje se katBroj, naslov, izdavac, godinaIzdavanja,
 a atribut izdat se podrazumevano stavlja na False. Uhvatiti izuzetak ukoliko je knjiga izdata u budućnosti 
 (proveriti preko datetime paketa).

Napraviti funkciju podesiIzdat(katBroj) koja podešava vrednost izdat i upisuje u bazu
 novu vrednost za datu knjigu.

Preko pandas paketa učitati sadržaj tabele knjige. 
Napraviti novi DataFrame objekat savremene_knjige koji će sadržati knjige kod kojih
 je godina izdavanja od 2000. godine.

Upisati u csv datoteku sve knjige koje su izdate u datoteku izdate_knjige.csv 
sa kolonama Naslov, izdavac, godinaIzdavanja
"""

from typing import Set
import pandas as panda
import sqlite3
from datetime import datetime

from pandas.io.pytables import Table

connection = sqlite3.connect("zadatak2/biblioteka.db")
cursor = connection.cursor()

trenutni_datum = datetime.now()
trenutna_godina = trenutni_datum.year


def ubaciNovuKnjigu():
    nastavi_petlju = ["Y", "y"]

    while True:
        with connection:
            odgovor = input("Da li želite da unesete novu knjigu ? -> y/n ")
            if odgovor in nastavi_petlju:
                katBroj = int(input("Unesite katBroj(int) : "))
                naslov = input("Unesite naslov : ")
                izdavac = input("Unesite izdavača : ")
                godina_izdavanja = int(input("Unesite godinu izdavanja : "))
                izdata = False
                try:
                    if(godina_izdavanja > trenutna_godina):
                        godina_izdavanja = trenutna_godina
                        raise Exception

                except Exception:
                    print(
                        "Uneli ste nedozvoljenu godinu(godinu veću od trenutne), zbog toga godina je podešena na trenutnu godinu.")
                    print(f"Trenutna godina je {trenutna_godina}.")
                cursor.execute("INSERT INTO knjige VALUES(?, ?, ?, ?, ?)",
                               (katBroj, naslov, izdavac, godina_izdavanja, izdata))

                connection.commit()
            else:
                break


def podesiIzdat(katBroj):
    if(katBroj != ""):
        with connection:
            cursor.execute("""UPDATE knjige
                           SET izdata = 1
                           WHERE katBroj = :katBroj""", {"katBroj": int(katBroj)})

            connection.commit()


cursor.execute("""CREATE TABLE IF NOT EXISTS knjige(
            katBroj integer,
            naslov text,
            izdavac text,
            godinaIzdavanja integer,
            izdata boolean
            )
""")

connection.commit()


ubaciNovuKnjigu()

katBroj = input(
    "Unesite katBroj knjige koju želite da izdate (polje može biti prazno ukoliko ne želite da menjate) :")
podesiIzdat(katBroj)

podaci = panda.read_sql_query(
    "SELECT * FROM knjige WHERE godinaIzdavanja > 2000", connection)

data_frame = panda.DataFrame(podaci)

print(data_frame)

podaci = panda.read_sql_query(
    "SELECT * FROM knjige", connection)

kolone_u_bazi = ["naslov", "izdavac", "godinaIzdavanja"]
izdate_knjige = podaci[podaci.izdata == 1][kolone_u_bazi]
izdate_knjige.to_csv("./zadatak2/izdate_knjige.csv")

connection.commit()
connection.close()
