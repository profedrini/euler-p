# -*- coding: utf-8 -*-
import time
from aritmetica import ListaPrimos  # En problema previo se precalculó tabla de primos menores que 10^6
from aritmetica import ConjuntoPrimos
from aritmetica import factoriza
from itertools import count

'''Dado que sabemos que la suma debe tener al menos 21 términos, necesariamente
los primos involucrados seran menos que 1000000/20  = 50000'''
t=time.time()

def menosque50000(p):
    if p < 5000:
        return True
    else:
        return False

P50000=list(filter(menosque50000, ListaPrimos))

Np=len(P50000)

SumasParciales = [sum(ListaPrimos[:k]) for k in range(Np)]

maxdiff=20
for a in range(Np-1,0,-1):
    for b in range(Np-2,0,-1):
        if SumasParciales[b]-SumasParciales[a] in ConjuntoPrimos:
            if b-a>maxdiff:
                print(b, a, b-a,SumasParciales[b]-SumasParciales[a])
                maxdiff=b-a
