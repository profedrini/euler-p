# -*- coding: utf-8 -*-
'''Problem 119
The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a number with this property is 614656 = 284.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.
'''

'''MORALEJA: Si los números son "raros", entonces en vez de probar muchos tratando de encontrarlos, 
mejor generarlos y trabajar con ellos'''

from math import log
from aritmetica import sumadigitos
from itertools import count
from math import floor

def probar(n,b):
    if b<2: return False
    while n>1:
        if n%b != 0:
            return False
        else:
            n = n/b
    return True
    
def check(n):
	b = sumadigitos(n)
	if b<2: return False
	return probar(n,b)
	
	
S=set()
for base in xrange(2,100):
    S=S.union([base**exponente for exponente in xrange(2,10) ])
S = S.difference(range(11))
S=filter(check, S)
S=list(S)
S.sort()

print S[1], S[9], S[29]

        