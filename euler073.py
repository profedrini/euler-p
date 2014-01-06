import time
from fractions import gcd
from fractions import Fraction
from aritmetica import GCD

T0= time.time()

def fracciones(d):
    return [(a,d) for a in range(d/3,d/2+1) if (d<3*a and 2*a<d and gcd(a,d)==1)]

L=[]    
S=0
for d in range(3,12001):
    L.extend(fracciones(d))

print len(L)
print time.time()-T0