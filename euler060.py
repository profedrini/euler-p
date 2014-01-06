from aritmetica import ListaPrimos
from itertools import combinations 

Primos=ListaPrimos[:20]
#def check(L):
print Primos

for p in combinations(Primos, 2):
    print p