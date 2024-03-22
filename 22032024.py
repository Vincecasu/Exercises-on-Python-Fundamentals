#Esempio di progetto segmentato
# 1) Sia data una lista <ls> contenente N digit da 1 a N
# non necessariamente tutti presenti quindi con 
# eventuali ripetizioni
# [1,2,3,4,5,6,7,8]
# N = 8 
# [1,1,2,2,3,5,7,8]

#Genera una lista che contiene N numeri casuali tra 1 e N
 
import random

def GeneraLista (N):
 lista = []

 for i in range(N):
        
        lista.append(random.randint(1,N))

 return lista

print (GeneraLista(10))

def Contauguali (ls, lscheck):

    uguali = 0

    for i in range (len (ls)):
        if lscheck[i] == ls[i]:
            uguali += 1
        return uguali
    
N = 8 
l1= GeneraLista(N)
l2= GeneraLista(N)

print (l1)
print (l2)

print (Contauguali (l1,l2))

# Conteggio e elimino gli elementi nello stesso posto

def ContaUgualiInStessoEInAltro(ls, lscheck):
    ls = ls.copy()
    lscheck = lscheck.copy()
    stessoposto = 0

    for i in range (len(lscheck)):

        if lscheck[i] == ls[i]:
            stessoposto += 1
            ls[i] = None
            lscheck [i] = None

# Conteggio e elimino gli elementi in posto differenti

    altroposto =  0   
    for i in range(len(lscheck)):
            if lscheck[i] != None and lscheck[i] in ls:
                altroposto += 1
                ls.remove(lscheck[i])
    return stessoposto, altroposto


N = 5
for i in range(4):
    l1 = GeneraLista(N)
    l2 = GeneraLista(N)
    print(l1)
    print(l2)
    stesso, diverso = ContaUgualiInStessoEInAltro(l1, l2)
    print(stesso, diverso)  


    