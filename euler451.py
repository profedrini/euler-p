from aritmetica import EsPrimo
from aritmetica import ConjuntoPrimos
from aritmetica import ListaPrimos
from itertools import imap

def l(n):
    if n in ConjuntoPrimos: 
        return 1
    for k in xrange(n-2,n//2,-1):
        if (k-1)%n ==0 or (k+1)%n==0 or (k*k-1)%n == 0:
            return k
    return 1


#print sum(imap(l, xrange(3,2*10**5+1)))
print l(15)