# Calcolare il Volume di una Botte, conoscendone i raggi e l'altezza

c = 3.1415

r1 = 30

r2 = 45

r3 = 33

h = 130


S1 = c * r1**2

S2 = c * r2**2

S3 = c * r3**2

V = (1/6)* h * (S1+ 4*S2 + S3) 

print (V)

litri = V/1000

print (litri)
