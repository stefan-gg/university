"""
Napisati funkciju srednja_vrednost(niz) koja vraća srednju vrednost elemenata niza.
Niz može biti lista celobrojnih ili razlomljenih brojeva. 
Koristiti pomoćnu promenljivu tmp koja akumulira vrednosti niza, element po element.
Uhvatiti izuzetak ukoliko element liste nije jedan od ovih tipova podataka (posebne izuzetke za tip string, 
list, dict, tuple), i vratiti posebne poruke.
U glavnom programu pozvati funkciju 4 puta sa različitim parametrima i pratiti 
vrednosti ulaznog parametra funkcije (niz) i tmp promenljive kroz debugger.
Screenshot-ovati nekoliko stanja debugger-a.
"""


def srednja_vrednost_niza(niz):
    try:
        broj_elemenata = 0
        suma = 0
        srednja_vrednost = 0
        greska = ""
        for tmp in niz:
            # rasporedio sam povratnu vrednost type funkcije uz pomos split("'")
            # i uzeo sam element koji se nalazi na poziciji 1
            # zato sto taj element predstavlja naziv tipa trenutnog elementa
            if(str(type(tmp)).split("'")[1] == "tuple"):
                greska = "tuple"
                raise TypeError
            elif(str(type(tmp)).split("'")[1] == "str"):
                greska = "string"
                raise TypeError
            elif(str(type(tmp)).split("'")[1] == "dict"):
                greska = "dictionary"
                raise TypeError
            elif(str(type(tmp)).split("'")[1] == "list"):
                greska = "list"
                raise TypeError
            else:
                suma += float(tmp)
                broj_elemenata += 1

        srednja_vrednost = (suma / broj_elemenata)

        return srednja_vrednost
    except TypeError:
        print("Nadjen je podatak tipa :" + greska +
              " što nije dozvoljeno za ovaj zadatak.")


print(srednja_vrednost_niza([1, 3, 12.2, "2","a"]))
print(srednja_vrednost_niza([1, 3, 12.2, ["stringgg"]]))
print(srednja_vrednost_niza([1, 3, 12.2, (12,)]))
print(srednja_vrednost_niza([1, 3, 12.2, 12, 31, 12.123]))
