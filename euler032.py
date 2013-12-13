# -*- coding: utf-8 -*-
from itertools import permutations

s = "123456789"
L=[]
for p in permutations(s):
    for k in range(1,9):
        for j in range(k+1,9):
            a= int("".join(p[:k]))
            b=int("".join(p[k:j]))
            c = int("".join(p[j:]))
            if a*b == c:
                L.append(c)
                #print (a,b,c)
print
L=list(set(L))
print L
print sum(L)