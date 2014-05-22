# -*- coding: utf-8 -*-
import itertools as it
import time

T0=time.time()
def X(n):
    return (n^(2*n))^(3*n)

'''X(n) regresará cero si y sólo si la expansión binaria de n no contiene dos 1 seguidos'''
'''Esta cuenta es conocida y por tanto la cantidad de n \le 2**30 
equivale a contar sucesiones binarias de longitud 30 que no contienen dos 1 seguidos,
cantidad que es igual a un número de Fibonacci'''


a,b=1,1
for n in range(30):
    a,b = b,a+b
print b

print time.time()-T0