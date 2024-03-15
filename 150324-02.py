#leggere da un file (persone.txt) i nomi , cognomi e eta di un gruppo di persone.
#organizzarli in un dizionario la cui chiave è il cognome e il cui valore è 
# una t-upla contenente i tre valori letti.

fin = open("persone.csv","r")
linee = fin.readlines()
fin.close()

lista = []
for l in linee:
     lista.append(l.strip().split(","))

print(lista)

for v in lista:
     persona = v.split(",")

     print("Nome: ", persona[0], ",Cognome: ", persona[1],",Età: ", persona[2])

 