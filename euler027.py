#coding=utf8
from aritmetica import *
import time
def cuentaprimos(a,b):
	'''Cuenta cuántos primos consecutivos hay
	al evaluar x^2 + ax + b   para x=0, 1, 2,...
	'''
	x = 0
	while True:
		s = x*x + a*x + b
		if s in ListaPrimos:
			x = x+1
		else:
			return x

t=time.time()
T=1000
mx = 2
for b in range(T):
	if b in ListaPrimos:
		for a in range(-T,T):
			cp=cuentaprimos(a,b)
			if cp>mx:
				print "(%d,%d) -> %d primos, producto = %d " % (a,b,cp,a*b)
				mx = cp

print time.time() -t , "segundos"
