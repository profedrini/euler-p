# -*- coding: utf-8 -*-
import time
t=time.time()

c = 1  # El while salta m=89, asi que lo añadimos desde el inicio.
top = 10**7
L={}
for k in [44,32,13,1,10]: L[k]=-1
for k in [85, 89, 145, 42, 20, 4, 16, 37, 58]: L[k]=1

def sumcuad(n):
	scuad = 0
	while n >0:
		ld = n%10
		scuad = scuad + ld*ld
		n = n/10
	return scuad

def sqchain(m):
    if m in L: return L[m]
    S = [m]
    while True:    
        sq = sumcuad(m)
        if sq in L:
            c = L[sq]
            for x in S:
                L[x] = c
            return c
        else:
            S.append(sq)
            m=sq

for n in xrange(2,top):
    sqchain(n)
    
print len([x for x in L if L[x]>0])
print time.time()-t
