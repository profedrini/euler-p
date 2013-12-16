# -*- coding: utf-8 -*-
import time
t=time.time()

c = 1  # El while salta m=89, asi que lo añadimos desde el inicio.
top = 10**7
L=[0]*(top)
for k in [44,32,13,1,10]: L[k]=-1
for k in [85, 89, 145, 42, 20, 4, 16, 37, 58]: L[k]=1

def sqchain(m):
    if L[m] != 0: return L[m]
    S = [m]
    while True:    
        sq = sum( [d*d for d in map(int,str(m))])
        if L[sq]!=0:
            c = L[sq]
            for x in S:
                L[x] = c
            return c
        else:
            S.append(sq)
            m=sq

for n in xrange(2, top):
    sqchain(n)
    
print len([x for x in L if x>0])
print time.time()-t