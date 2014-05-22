# -*- coding: utf-8 -*-
'''Problem 127
The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

We shall define the
triplet of positive integers (a, b, c) to be an abc-hit if:

GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
a < b
a + b = c
rad(abc) < c
For example, (5, 27, 32) is an abc-hit, because:

GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
5 < 27
5 + 27 = 32
rad(4320) = 30 < 32
It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.

Find ∑c for c < 120000.
'''
import time
T0 = time.time()
from aritmetica import factoriza
from operator import mul
from fractions import gcd

def radical(n):
    D=factoriza(n)
    return reduce(mul, D.keys(), 1)

T1 = time.time()

S=0    
k = 0
hits = []
for c in xrange(3,120000):
    for b in xrange((c+1)//2,c):   # b tiene que ser mayor o igual a la mitad de c para que a<b
        #if gcd(b,c)!=1: continue
        a = c-b                    # a + b = c
        if gcd(a,b)==1  :
            if radical(a*b*c)< c:
                k=k+1
                S=S+c
                #hits.append(c)

print k,S
T3 = time.time()
print T3-T0, T3-T1