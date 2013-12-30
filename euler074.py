# -*- coding: utf-8 -*-
'''The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; 
it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. 
For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, 
but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, 
contain exactly sixty non-repeating terms?
'''

from aritmetica import factorial
from aritmetica import digitos
import time
Tt=time.time()
D = {}

def f(n):
    return sum(map(factorial, digitos(n)))

def check(n):
    if n in D:  # Si ya conocemos la dinámica de n, al siguiente
        return 
    # Entonces no conocemos la dinámica que inicia en n...
    m=n
    L=[m]
    #print "\n",m,
    while True:
        m=f(m)
        #print m,
        if m in D:
            # Si caemos en un conocido, terminamos
            k=D[m]
            for x in L[::-1]:
                k=k+1
                D[x] = k
            return

        if m in L:
            # Ya se reptitió la lista, sin caer en uno conocido previamente
            k=0
            for x in L[::-1]:
                 k=k+1
                 D[x]=k
            return
        L.append(m)

for k in xrange(1,10**6):
    check(k)

print len([x for x in D if D[x]==60])
print time.time()-Tt