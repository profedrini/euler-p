from aritmetica import digitos
from collections import Counter

C = {}
#Fill the dictionary
SOLUTIONS = set()

for n in xrange(2,10000):
	z=tuple(sorted(digitos(n**3)))
	D= C.get(z,[])
	D.append(n)
	C[z] = D

MINI = 100000000
for k in C:
	if len(C[k])==5: 
		newmin = min(C[k])
		if newmin < MINI:
			MINI = newmin

print MINI**3
