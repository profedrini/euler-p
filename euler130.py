from aritmetica import ConjuntoPrimos
from itertools import count
from fractions import gcd
import time

Tt=time.time()

def R(n):
    return (10**(n)-1)/9

    
def A(n):
    
    for k in xrange(1,n):
        if R(k)%n == 0 : 
            return k
    return False

c=0
S=0
for n in xrange(3,10**6,2):
    if n not in ConjuntoPrimos and gcd(n,10)==1:
        v=A(n)
        if v:
            if (n-1)%v==0:
                c=c+1
                S=S+n
                print "%d: %d, %d" % (c,n,v)
                if c ==25: break
            
print S
print time.time()-Tt