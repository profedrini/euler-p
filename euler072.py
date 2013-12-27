from aritmetica import totient

import time
T=time.time()
c=0
for n in xrange(2,10**6+1):
    c = c+totient(n)

print c
print time.time()-T
        