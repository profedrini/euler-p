from aritmetica import ListaPrimos
from aritmetica import ConjuntoPrimos
from itertools import *
import math
from aritmetica import EsPrimo
def check(p, verbose=False):
	'''for d in [2,4,6,8,0]:
		if d in map(int, str(p)):
			return False
	
	'''# Verifiquemos por la izquierda:
	m=p
	while(m>0):
		if verbose: print m,
		if  not EsPrimo(m):
			return False
		m = (m - m%10) // 10
	if verbose: print
	# Verifiquemos por la derecha:
	m=p
	k = int(math.floor(math.log10(m)))  # n tiene k cifras
	for i in range(k,0,-1):
		m= m%(10**i)
		if verbose: print m,
		if not(EsPrimo(m)):
			return False
	if verbose: print
	return True


S = 0
c=0
digits = ["2","1","3","5","7","9"]

for k in range(2,7):
	for l in product(digits, repeat=k):
		n=int("".join(l))
		if n%3==0 or n%5 ==0 or n%7==0 or n%11 ==0 or n%13 ==0 or n%17 ==0:
			pass
		else:
			if check(n):
				c=c+1
				S=S+n 
				print n

print (c,S)

