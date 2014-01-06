from aritmetica import ListaPrimos
from itertools import ifilter

L1 = filter(lambda p : p<7071, ListaPrimos)
L2 = filter(lambda p : p<368, ListaPrimos)
L3 = filter(lambda p : p<84, ListaPrimos)

TOP = 50*10**6
D = {}
for c in L3:
    for b in L2:
        bc = b**3 + c**4
        if bc >= TOP: break
        for a in L1:
            abc = a**2 + bc
            if abc >= TOP: 
                break
            else:
                D[abc]=True

print len(D)            
