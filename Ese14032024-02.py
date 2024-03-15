#Dato alice.txt , stampare , una per riga ,
#tutte le parole che lo compongono

fin = open("alice.txt","r")
linee = fin.readlines()
fin.close()

lista = []
for l in linee:
    lista.extend(l.split(" "))

print(lista)

ls = ["uno","","due","","tre","","", "","  "," fine"]

lnuova = []

for i in ls:
    if len (i.strip()) > 0 :
        lnuova.append(i)

print (lnuova)

    
#Contare quanti caratteri ci sono in Alice.txt
#Contare quanti caratteri non spazi bianchi ci sono in alice.txt
#Contare quanti caratteri alfanumerici [a-zA-Z0-9] ci sono in alice.txt

fin = open("alice.txt","r")
linee = fin.read()
fin.close()








