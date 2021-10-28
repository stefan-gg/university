import random

lista_brojeva = []
sortirana_lista = []
for broj in range(4056):
    dodaj_u_listu = random.randint(-10000, 10000)
    lista_brojeva.append(dodaj_u_listu)
print("*************************************************************************************************")
print("Lista pre sortiranja ->", lista_brojeva)
max = -10001

while(True):
    if(len(lista_brojeva) == 0):
        break
    for i in range(len(lista_brojeva)):
        if(max < lista_brojeva[i]):
            max = lista_brojeva[i]
    
    sortirana_lista.append(max)
    lista_brojeva.remove(max)
    max = -10001
lista_brojeva = sortirana_lista
print("*************************************************************************************************")
print("Lista posle sortiranja ->", lista_brojeva)