# -*- coding: utf-8 -*-
'''
Consider the infinite polynomial series AF(x) = xF1 + x2F2 + x3F3 + ..., where Fk is the kth term in the Fibonacci sequence: 1, 1, 2, 3, 5, 8, ... ; that is, Fk = Fk−1 + Fk−2, F1 = 1 and F2 = 1.

For this problem we shall be interested in values of x for which AF(x) is a positive integer.

Surprisingly AF(1/2)	 = 	(1/2).1 + (1/2)2.1 + (1/2)3.2 + (1/2)4.3 + (1/2)5.5 + ...
 	 = 	1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...
 	 = 	2'''
 
'''Usando la función generadora y resolviendo AF(x) = n, obtenemos que para que las
raíces sean racionales, el discriminante 5n^2 + 2n +1 debe ser un cuadrado perfecto'''

from itertools import count
from math import sqrt
from math import floor
import time
T0=time.time()
Cuadrados = {n*n for n in xrange(10**8)}
print "Precálculo de cuadrados:", time.time() - T0
T1=time.time()
def EsCuadrado(m):
    if m<10**16:
        if m in Cuadrados:
            return True
        else:
            return False    

    if m%3 == 2: return False
    if m%8 not in {0,1,4} : return False
    if m%10 not in {0,1,4,5,6,9} : return False
    
    v=sqrt(m)
    if v-floor(v)>0:
        return False
    else:
        return True

def discri(n): return 5*n**2 + 2*n+1

c=0
for n in count(1):
    if n%3 ==1: continue
    if n%5 ==1 or n%5 ==3 : continue
    
    if EsCuadrado(5*n**2 + 2*n+1):
        c+=1
        print c,n, time.time()-T1
        if c ==15: break

print "tiempo total:", time.time()-T0