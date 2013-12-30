# -*- coding: utf-8 -*-
'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''
from itertools import count

N=50000

Triangulos = set([n*(n+1)/2 for n in xrange(5*N)])
Pentagonos = set([n*(3*n-1)/2 for n in xrange(5*N)])

def Hexagonos():
    for n in count(1):
        yield n*(2*n-1)
        
for k,h in enumerate(Hexagonos()):
    if (h in Triangulos) and (h in Pentagonos):
        print (k+1,h)
    if k>N: break
    