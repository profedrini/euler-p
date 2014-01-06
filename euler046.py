from aritmetica import ListaPrimos
from aritmetica import ConjuntoPrimos
from itertools import count
from aritmetica import EsPrimo
TOP=10**6
D={p+2*a*a:True for p in ListaPrimos[:1000] for a in xrange(1,10**3)}

print ".."
for n in xrange(9,TOP,2):
    if n not in D:
        if not(n in ConjuntoPrimos):
            print n
            break