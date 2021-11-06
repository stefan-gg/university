class Dokument():
    def __init__(self, ime, broj_reci):
        self.ime = ime
        self.broj_reci = broj_reci
    
class Knjiga(Dokument):
    def __init__(self, ime, broj_reci, autor, zanr, godina_izdavanja):
        super().__init__(ime, broj_reci)
        self.autor = autor
        self.zanr = zanr
        self.godina_izdavanja = godina_izdavanja

    '''
    napravio sam ovu funkciju budući da se ona poziva kada želimo da štampamo objekat,
    kako bi štampala u određenom formatu objekat odnosno njegov sadržaj
    '''
    def __str__(self):
        return ": " + self.zanr + ", " + self.autor + ", " + self.ime + "."

knjiga1 = Knjiga("Knjiga o nauci", 21, "Stefan", "Triler", 2019)
knjiga2 = Knjiga("Enciklopedija", 21, "Stefan", "Triler", 2011)
knjiga3 = Knjiga("Enciklopedija o dinosaurusima", 21, "Stefan", "Triler", 2012)
knjiga4 = Knjiga("1000 zašto 1000 zato", 21, "Stefan", "Triler", 2013)
knjiga5 = Knjiga("Koreni", 21, "Stefan", "Triler", 2001)
knjiga6 = Knjiga("Pitam se zašto", 21, "Stefan", "Triler", 2009)
knjiga7 = Knjiga("Derviš i smrt", 21, "Stefan", "Triler", 2010)
knjiga8 = Knjiga("Knjiga o životinjama", 21, "Stefan", "Triler", 2016)
knjiga9 = Knjiga("Zvezde i planete", 21, "Stefan", "Triler", 2015)
knjiga10 = Knjiga("Orlovi rano lete", 21, "Stefan", "Triler", 2020)

library = {}
library.update({"lib001" : knjiga1})
library.update({"lib002" : knjiga2})
library.update({"lib003" : knjiga3})
library.update({"lib004" : knjiga4})
library.update({"lib005" : knjiga5})
library.update({"lib006" : knjiga6})
library.update({"lib007" : knjiga7})
library.update({"lib008" : knjiga8})
library.update({"lib009" : knjiga9})
library.update({"lib010" : knjiga10})


for i,x in library.items():
    print(i, x)

