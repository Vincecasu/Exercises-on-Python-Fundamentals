#In una stanza entrano ,uno dopo l'altro ,10 persone,rispettivamente:
#antonio ,marco,andrea,luigi,tony,bruno,laura,anita,annarita,lucia
#le prime due vanno via dopo un pochino di tempo ma entrano altre tre persone
#john ,alice , mary
#alre due vanno via, sempre in ordine di ingresso(primo entrato, primo a uscire)
#stampare l'elenco delle persone presenti
#per generare un numero casuale tra 10 e 20 ,20 incluso : random.randint(10,20)
#per generare un numero casuale tra 0 e 1 : random.random()

stanza = []
stanza.append("Antonio")
stanza.append("Marco")
stanza.append("Andrea")
stanza.append("Luigi")
stanza.append("Tony")
stanza.append("Bruno")
stanza.append("Laura")
stanza.append("Anita")
stanza.append("Annarita")
stanza.append("Lucia")

stanza = stanza[2:]

stanza.append("john")
stanza.append("alice")
stanza.append("mary")

stanza = stanza[2:]

print(stanza)

stanza.sort()

print(stanza)

### Seconda versione
stanza = [
    "antonio",
    "marco",
    "andrea",
    "luigi",
    "tony",
    "bruno",
    "laura",
    "anita",
    "annarita",
    "lucia",
]
stanza = stanza[2:]
stanza.extend(["john", "alice", "mary"])
stanza = stanza[2:]
print(stanza)
stanza.sort()
print(stanza)
