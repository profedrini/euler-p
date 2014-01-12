# -*- coding: utf-8 -*-

import itertools
import time
T0=time.time()

Pesos={}
archivo = open("matrix.txt")
for (i,l) in enumerate(archivo):
    L=map(int,l.split(","))
    Pesos.update({ (i,j):k for (j,k) in enumerate(L)})
archivo.close()

nRows = 80
nCols = 80
TARGET = (79,79)

Aristas = { (i,j):[(i+1,j),(i,j+1)] for (i,j) in itertools.product(xrange(nRows-1),xrange(nCols-1))}
for r in xrange(nRows-1):
    Aristas[(r,nCols-1)]=[(r+1,nCols-1)]
for c in xrange(nCols-1):
    Aristas[(nRows-1,c)]=[(nRows-1,c+1)]
Aristas[(nRows-1, nCols-1)]=[]

Sumas = {(0,0):Pesos[(0,0)]}
actual=(0,0)
Visited = set()
Tentativos = set()

while actual != TARGET:
    for u in Aristas[actual]:
        if u not in Visited:
            if u not in Sumas:
                Sumas[u] = Sumas[actual] + Pesos[u]
                Tentativos.add(u)
            else:
                newsuma = Sumas[actual] + Pesos[u]
                if newsuma < Sumas[u]:
                    Sumas[u]=newsuma
                    Tentativos.add(u)
    
    Visited.add(actual)
    Tentativos.discard(actual)
    actual = min(Tentativos, key=Sumas.get)

print Sumas[actual]
print time.time()-T0, "segundos"