ispiti_dict = {}

broj_ispita = int(input("Unesite broj polozenih ispita >> "))

for broj in range(broj_ispita):
    sifra_predmeta = input("Unesite sifru predmeta >> ")
    dobijena_ocena = int(input("Unesite ocenu koju ste dobili iz predmeta >> "))

    ispiti_dict.update({sifra_predmeta : dobijena_ocena})

pregled_ocene = input("Unesite sifru predmeta iz kojeg zelite da pregledate ocenu >> ")

for ispit in ispiti_dict.keys():
    if(ispit == pregled_ocene):
        ocena = ispiti_dict[ispit]
        if(ocena > 5 and ocena < 11):
            print("Ispit je polozen")
        else:
            print("Ispit nije polozen")
