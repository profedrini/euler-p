from aritmetica import EsPrimo
from itertools import permutations
digits=map(str,range(1,10))


for k in range(9,7,-1):
	stop=False
	for p in permutations(digits,k):
		n = int("".join(p))
		if EsPrimo(n): 
			print n
			stop=True
	if stop: break
print digits
