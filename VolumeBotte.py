# Calcolare il Volume di una Botte, conoscendone i raggi e l'altezza

r1 = (int (input ("r1 = ")))

r2 = (int (input ("r2 = ")))

r3 = (int (input ("r3 = ")))


c = 3.1415



h = 130


S1 = c * r1**2

S2 = c * r2**2

S3 = c * r3**2

V = (1/6)* h * (S1+ 4*S2 + S3) 

print (V)

litri = V/1000

print (litri)
