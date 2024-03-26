# Progetto da svolgere
"""
Il gioco del master mind consiste in:
- N palline colorate (i nostri digit)
- M caselle da riempire (la lunghezza delle nostre liste)
- una sequenza di M palline colorate generata dal master del gioco
- un ciclo di prove in cui
    1) il giocatore fornisce la sua proposta
    2) il master verifica il numero di strike e ball ottenuti
    3) il master comunica strike e ball al giocatore
    4) se sono M strike, il giocatore ha vinto
        5) altrimenti si riparte da 1, con la nuova proposta
- Esempio di gioco
    N=6 (sei simboli, da 1 a 6)
    M=4 (lunghezza delle liste pari a 4)
    master= GeneraLista(4, 6)
        - quindi master potrebbe essere ad esempio [4,1,1,5]
    ciclo di gioco
        1) il giocatore comunica "1234" che viene trasformato in [1,2,3,4]
        2) [1,2,3,4] vs [4,1,1,5] => 0 strike, 2 ball
        3) non ha vinto poichè servono M strike
        4) il giocatore ricomincia al punto 1, stavolta,
           ovviamente, con una nuova proposta, es 2156 => [2,1,5,6]
        ecc, ecc, ecc
"""
import random



# Esempio di utilizzo:
#sd = input("Inserisci la tua prova: ")
#print(ConvertiStringaDigitInListaNumeri(sd))

def GeneraLista (M,N):
 
 lista = []

 for i in range(M):
       
       lista.append(random.randint(1,N))

 return lista

def ConvertiStringaDigitInListaNumeri(sd):
    return [int(x) for x in list(sd)]

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
   


N = int(input("Inserire il numero di simboli: "))
M = int(input("Inserire la lunghezza della lista: "))
l1 = GeneraLista(N, M)
strike = 0 
while strike!= M:
    l2 = input("Inserire la tua prova :")
    lista = ConvertiStringaDigitInListaNumeri(l2)
    strike, ball = ContaUgualiInStessoEInAltro(l1, lista)
    print("Strike: ", strike, "Ball: ", ball)
print("Hai vinto! ", l1)
