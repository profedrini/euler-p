from itertools import *

N = 9
coins = range(1,N)


def paga(n, allowed, level=1):
	'''regresa las formas de pagar $n usando monedas menores o iguales a $top)'''
	L=[]
	if n<1: return [[]]
	for (i,a) in enumerate(allowed):
		#if level==1: print a,
		if a > n:
			pass
		else:
			suballowed = allowed[i:]
			SL=paga(n-a, suballowed,level+1)
			nuevas=[ [a]+s for s in SL ]
			L.extend(nuevas)
	return L

U=paga(N,coins)
#print U
print
print len(U)
