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
TARGET = (100,100)
START = (-1,-1)

Pesos.update({START:0, TARGET:0})
Sumas = {START:0}
actual=START
Visited = set()
Tentativos = set()

Aristas = { (i,j):[(i-1,j), (i,j+1),(i+1,j),(i,j-1)] for (i,j) in itertools.product(xrange(1,nRows-1),xrange(1,nCols-1))}

    
for c in xrange(1,nCols-1):
    Aristas[(0,c)]=[(0,c+1), (1,c),(0,c-1)]  # Nodos de la fila superior
    Aristas[(nCols-1,c)]=[(nCols-1,c+1), (nCols-1,c-1),(nCols-2,c)]  # Nodos de la fila inferior
    
for r in xrange(nRows-1):
    Aristas[(r,0)]=[(r,1),(r+1,0)]  # Nodos de la fila izquierda
    Aristas[(r,nRows-1)] = [(r+1,nRows-1),(r,nRows-2)]   # Nodos de la fila derecha
Aristas[(nRows-1,0)]=[(nRows-1,1)]
Aristas[START] = [(0,0)]
Aristas[(nRows-1,nCols-1)]=[TARGET]

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