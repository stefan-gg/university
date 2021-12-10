import pandas as pd

predmeti_i_ocene = []
validni_odgovori = {"Y", "y"}
validne_ocene = {"6", "7", "8", "9", "10"}

while(True):
    dodaj_novi_ispit = input("Dodaj novi položeni ispit ?(Y/N) > ")

    if dodaj_novi_ispit in validni_odgovori:
        ime_predmeta = input("Unesite ime predmeta > ")
        ocena = input("Unesite ocenu (minimum je 6 a maximum je 10) >")
        if ocena in validne_ocene:
            ocena = int(ocena)
            predmeti_i_ocene.append({"Predmet": ime_predmeta, "Ocena": ocena})
        else:
            print("Uneli ste nevažeću vrednost za ocenu !!")
            continue
    else:
        break

data_frame = pd.DataFrame.from_dict(predmeti_i_ocene)
data_frame.to_csv("Student_izvestaj.csv", index=False, header = True)
