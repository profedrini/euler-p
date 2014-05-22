from operator import mul
from aritmetica import factoriza
import os
import time

T0 = time.time()
S = {1}
Fila = [1]

def IsSquareFree(n):
    F = factoriza(n)
    for p in F:
        if F[p]>1:
            return False
    return True

for k in range(51):
    Fila = [0] + Fila[:] + [0]
    #print "\t",Fila    
    newfila =[Fila[i]+Fila[i+1] for i in range(k+1)]
    Fila = newfila[:]
    #print newfila
    S = S.union(newfila)
    

total=len(S)
print sum(filter(IsSquareFree, S))