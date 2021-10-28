import random
import array as arr

def sort(ime, br_indeksa):
    max = 100000

    # dif_prva2 = br_indeksa // 1000 -  (br_indeksa // 100) % 10
    # if(dif_prva2 > 0):
    #     dif_prva2 *= -1

    # suma_zadnja_2 = br_indeksa % 10 +  ((br_indeksa % 100) // 10)

    if(len(ime) % 2 == 0):
        brojevi = arr.array("i", [])
        sortirani_niz = arr.array("i", [])
        
        for i in range(0, br_indeksa):
            brojevi.append(random.randint(0, br_indeksa))
    else :
        brojevi = arr.array("f", [])
        sortirani_niz = arr.array("f", [])
        
        for i in range(0, br_indeksa):
            brojevi.append(random.uniform(-1 * (br_indeksa / 100), br_indeksa % 100))#dif_prva2, suma_zadnja_2))

    while(True):
        if(len(brojevi) == 0):
            break
        for i in range(len(brojevi)):
            if(max > brojevi[i]):
                max = brojevi[i]

        sortirani_niz.append(max)
        brojevi.remove(max)
        max = 100000
    
    brojevi = sortirani_niz

    return brojevi

ime = input("Unesite ime : ")
br_ind = int(input("Unesite broj indeksa : "))

main_deo = sort(ime, br_ind)

print(main_deo)