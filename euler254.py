from aritmetica import digitos
from aritmetica import Factoriales
from aritmetica import sumadigitos

def f(n):
    return sum([Factoriales[d] for d in digitos(n)])
    
def sf(n):
    return sumadigitos(f(n))


L = [sf(n) for n in xrange(100000000)]
G = [L.index(i) for i in xrange(0,151)]
print G
print sum([sumadigitos(G[k]) for k in xrange(1,151)])