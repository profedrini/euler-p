# -*- coding: utf-8 -*-
# Creamos el conjunto de los primeros 1000 números triangulares
triangles =set([k*(k+1)/2 for k in range(1000)])

def valor(c):
    return ord(c)-64    # Valor de la letra c
    

def palabra(w):
    return sum(map(valor,w))  # Valor de la palabra w

def EsTriangular(w):
    v = palabra(w)
    return (v in triangles)
        
with open("words.txt") as f:
    data=f.read()   # Lee el texto en data
    
data=data.replace('"',"").split(",")  # elimina comillas, crea lista separando en comas
trianglewords = filter(EsTriangular, data)  # Filtra con el predicado EsTriangular
print len(trianglewords)

