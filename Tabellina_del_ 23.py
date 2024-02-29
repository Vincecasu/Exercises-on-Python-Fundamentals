#Esercizio
#Stampare la tabellina del 23.

import random


for i in range(23,231,23):
    print (i, end=" ")
print()

#Esercizio
#sapendo che la funzione random.randint(start, end)
#genera un numero intero compreso tra start e end, end compreso
#costruire una lista di numeri casuali lunga 100 e
#stampare la somma di tutti i suoi numeri.

lista = []

for i in range(100):
    lista.append(random.randint(1, 10))

#Sommare tutti i valori
totale = 0
for i in lista:
    totale = totale + i
print ("totale ", )


#Esercizio 

listapari = []

for i in range(0):
    print (i+1)




