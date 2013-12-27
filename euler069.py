from aritmetica import totient
from operator import truediv

MAX = 2

for n in xrange(1,10**6+1):
    tn = totient(n)
    u=truediv(n,tn)
    if u > MAX:
        print n, tn, u
        MAX=u
        