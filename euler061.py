# -*- coding: utf-8 -*-
'''Problem 61

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:

Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square	 	P4,n=n2	 	1, 4, 9, 16, 25, ...
Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
'''
from aritmetica import digitos

TRIANGS = [str(n*(n+1)/2) for n in range(45,141)]
CUADS = [str(n*n) for n in range(32,101)]
PENTAS = [str(n*(3*n-1)/2) for n in range(24,82)]
HEXAS = [str(n*(2*n-1)) for n in range(23,71)]
HEPTAS = [str(n*(5*n-3)/2) for n in range(21,64)]
OCTAS = [str(n*(3*n-2)) for n in range(19,59)]

L = [TRIANGS, CUADS, PENTAS, HEXAS, HEPTAS, OCTAS]


def CheckPrefijo(s,x):
#	if set(s[-2:])==set(x[:2]):
        if s[-2:] == x[:2]:
		return True
	else:
		return False


def Forward(s,track, chain):
    #print "last:",s, "cadena:", chain, track
    if not(any(track)): 
        if CheckPrefijo(chain[-1],chain[0]):
            print "DING!", chain, sum(map(int,chain))
            return chain #Se agoto la cadena
    prevtrack = track[:]
    for k in range(6):
        if prevtrack[k]>0:
            # Buscamos en la k-esima lista
            #print "\t checking list",k,
            moves = [x for x in L[k] if CheckPrefijo(s,x)]
            #print moves
            if len(moves)>0:  # Si podemos avanzar
                nextrack = track[:]
                nextrack[k] = 0   # Ya no podemos volver a tomar de esta lista
                for m in moves:
                    cadena = chain[:] + [m]
                    Forward(m, nextrack, cadena)

# Dado que la  cadena es cíclica, podemos comenzar
# revisando en cualquiera de las listas, y sólo hay que avanzar, 
# no es necesario verificar en dirección contraria.
for a in OCTAS:
    TRACK=[1,1,1,1,1,0]
    CHAIN = [a]
    Forward(a, TRACK, CHAIN)

