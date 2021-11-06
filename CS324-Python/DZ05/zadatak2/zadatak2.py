class Osoba():
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime


class Student(Osoba):
    def __init__(self, ime, prezime, broj_indeksa, smer, polozeni_ispiti):
        super().__init__(ime, prezime)
        self.broj_indeksa = broj_indeksa
        self.smer = smer
        self.polozeni_ispiti = polozeni_ispiti

#funkcija koja proverava broj položenih ispita
def broj_polozenih_ispita(ispiti):
    broj_polozenih_ispita = 0
    
    for ocena in ispiti.values():
        if(ocena > 5 and ocena <= 10):
            broj_polozenih_ispita += 1
    return broj_polozenih_ispita

def provera_istih_polozenih_ispita(ispiti_prvog_studenta, ispiti_drugog_studenta):
    broj_istih_polozenih_ispita = 0
    poruka = "Oba studenta su položila sledeće ispite : "

    for ime_ispita, ocena in ispiti_prvog_studenta.items():
        if(ocena > 5 and ocena <= 10):
            if ime_ispita in ispiti_drugog_studenta:
                if(ispiti_drugog_studenta[ime_ispita] > 5 and ispiti_drugog_studenta[ime_ispita] <= 10):
                    broj_istih_polozenih_ispita += 1
                    poruka += "->" + ime_ispita + " "

    if(broj_istih_polozenih_ispita == 0):
        print("Studenti nemaju zajedničke položene ispite")
    else:
        print(poruka)

prvi_student = Student("Stefan", "Gogić", 9999, "IT", {
                       "CS324": 9, "CS101": 5, "CS102": 7, "CS225": 10, "SE201" : 6})
drugi_student = Student("Ime", "Prezime", 2812, "SE", {
                        "CS324": 6, "IT370": 5, "IT331": 7, "CS225": 10})

if(prvi_student.smer == drugi_student.smer):
    print("Studenti se nalaze na instom smeru")
else:
    print("Studenti se ne nalaze na instom smeru")

print(broj_polozenih_ispita(prvi_student.polozeni_ispiti))
print(broj_polozenih_ispita(drugi_student.polozeni_ispiti))

provera_istih_polozenih_ispita(prvi_student.polozeni_ispiti, drugi_student.polozeni_ispiti)

