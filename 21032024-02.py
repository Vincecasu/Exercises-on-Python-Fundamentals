def somma (n):
    if n == 0:
        return 0
    else:
        return somma (n-1) + n

print (somma(10))