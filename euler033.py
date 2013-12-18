from fractions import *
from operator import mul
L = []
for a in xrange(1,10):
	for b in xrange(a+1,10):
		for d in xrange(1,10):

			u,v  = 10*a+d, 10*b+d
			if Fraction(u,v) == Fraction(a,b):
				L.append(Fraction(a,b))

			u,v  = 10*a+d, 10*d+b
			if Fraction(u,v) == Fraction(a,b):
				L.append(Fraction(a,b))
			u,v  = 10*d+a, 10*b+d
			if Fraction(u,v) == Fraction(a,b):
				L.append(Fraction(a,b))
			u,v  = 10*d+a, 10*d+b
			if Fraction(u,v) == Fraction(a,b):
				L.append(Fraction(a,b))

print reduce(mul, L)
