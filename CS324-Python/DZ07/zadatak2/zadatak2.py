import sqlite3
from sqlite3.dbapi2 import connect

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()


def vratiPodatkeZaProfesora(ime_profesora):
    cursor.execute("SELECT * FROM predmeti WHERE profesor = :profesor", {
        "profesor": ime_profesora
    })
    connection.commit()
    return cursor.fetchall()


cursor.execute("""CREATE TABLE predmeti(
        sifra text,
        puno_ime text,
        profesor text,
        godina_studija number
        )""")

connection.commit()

predmeti = {"CS324": ["Skripting jezici", "Nemanja Zdravković", 3],
            "IT255": ["Veb sistemi 1", "Vladimir Milićević", 3],
            "IT350": ["Baze podataka", "Milena Bogdanović", 2],
            "CS220": ["Arhitektura računara", "Nemanja Zdravković", 2],
            "SE201": ["Softversko inženjerstvo", "Dragan Domazet", 2],
            "NT111": ["Engleski 1", "Dubravka Vlahović", 1],
            "MA104": ["Matematika 1", "Dušan Simjanović", 1]
            }

for ime_predmeta, podaci in predmeti.items():
    cursor.execute("INSERT INTO predmeti VALUES (?, ?, ?, ?)",
                   (ime_predmeta, podaci[0], podaci[1], podaci[2]))

    connection.commit()

rezultat = vratiPodatkeZaProfesora("Dubravka Vlahović")
print(rezultat)
