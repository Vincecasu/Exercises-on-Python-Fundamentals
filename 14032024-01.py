fin = open("alice.txt","r")
linee = fin.readlines()
fin.close()

l1 =[]
for l in linee:
    l1.append(l.strip())

    linee = l1
print(linee)


