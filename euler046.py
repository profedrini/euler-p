from aritmetica import ListaPrimos
from aritmetica import ConjuntoPrimos
from itertools import count
from aritmetica import EsPrimo
TOP=10**7
D={p+2*a:True for p in ListaPrimos[:500] for a in xrange(10**4)}

print ".."
for n in xrange(9,TOP,2):
    if n not in D:
        print D