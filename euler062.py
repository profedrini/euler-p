'''Problem 62
The cube, 41063625 (345^3), can be permuted to produce two other cubes:
    56623104 (384^3) and 66430125 (405^3). 
    In fact, 41063625 is the smallest cube which has exactly three permutations 
    of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''
from itertools import permutations
from aritmetica import digitos
from operator import mul
from aritmetica import factorial

print "precalculando..."

CUBOS = {n**3 for n in range(10**9)}
DIGITOS=[1,2,3,4,5,6,7,8,9,0]
D={}

def lista2num(L):
    l=L[::-1]
    return     sum( [a*10**(k) for (k,a) in enumerate(l)])

def overcount(p):
    repeticiones= map(factorial, filter(lambda x: x>1, [p.count(d) for d in range(10)]))
    sobreconteo = reduce(mul, repeticiones, 1)

    return sobreconteo

for n in xrange(1,1000):
    dig = digitos(n**3)
    #print dig
    v={lista2num(p) for p in permutations(dig) if lista2num(p) in CUBOS and p[0]!=0}
    ncubos = len(v)
    #print n, n**3, "\t",len(v), ncubos, v
    if ncubos == 5: 
        print n
        break
        
print overcount(digitos(345**3))
print 345**3