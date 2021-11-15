"""
Zadatak #1
Napisati program koji će praviti Vaš raspored časova i sačuvati kao CSV datoteku.
Otvoriti CSV datoteku u programu Excel (ili sličnom programu) kao dokaz da je uspešno napravljena datoteka.
"""
import csv

dani = ['Vreme', 'Ponedeljak', 'Utorak', 'Sreda', 'Četvrtak', 'Petak']
termini = ["9:50-10:30", "10:40-11:20", "11:30-12:10", "12:20-13:00",
           "13:10-13:50", "14:00-14:40", "14:50-15:30", "15:40-16:20", "16:30-17:10",
           "17:20-18:00", "18:10-18:50", "19:00-19:40"]

predmeti_i_broj_casova = {"CS225": 5, "CS324": 6, "IT255": 6, "IT335": 4}

raspored_za_termin = []

cs225 = cs324 = it255 = it335 = False

with open('zadatak1/raspored.csv', 'w', encoding="UTF-8") as raspored:
    upis = csv.writer(raspored)
    upis.writerow(dani)

    for vreme in termini:
        raspored_za_termin.append(vreme)

        if("9:50" in vreme):
            cs324 = True
        if("12:20" in vreme):
            it335 = True
        if("14:00" in vreme):
            it255 = True
        if("15:40" in vreme):
            cs225 = True

        if(it255 == True):
            if(predmeti_i_broj_casova.get("IT255") > 0):
                raspored_za_termin.append("IT255")
                predmeti_i_broj_casova.update(
                    {"IT255": predmeti_i_broj_casova.get("IT255") - 1})
            else:
                it255 = False
                raspored_za_termin.append("x")
        else:
            raspored_za_termin.append("x")

        if(cs324 == True):
            if(predmeti_i_broj_casova.get("CS324") > 0):
                raspored_za_termin.append("CS324")
                predmeti_i_broj_casova.update(
                    {"CS324": predmeti_i_broj_casova.get("CS324") - 1})
            else:
                cs324 = False
                raspored_za_termin.append("x")
        else:
            raspored_za_termin.append("x")

        raspored_za_termin.append("x")

        if(it335 == True):
            if(predmeti_i_broj_casova.get("IT335") > 0):
                raspored_za_termin.append("IT335")
                predmeti_i_broj_casova.update(
                    {"IT335": predmeti_i_broj_casova.get("IT335") - 1})
            else:
                it335 = False

        if(cs225 == True):
            if(predmeti_i_broj_casova.get("CS225") > 0):
                raspored_za_termin.append("CS225")
                predmeti_i_broj_casova.update(
                    {"CS225": predmeti_i_broj_casova.get("CS225") - 1})
            else:
                cs225 = False
        else:
            if(it335 == False):
                raspored_za_termin.append("x")

        raspored_za_termin.append("x")
        upis.writerow(raspored_za_termin)
        raspored_za_termin.clear()
