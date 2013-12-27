from fractions import Fraction
from aritmetica import ndigitos

def f(r):
    return 1+1/(1+r)

a = Fraction(3,2)

c=0
for r in xrange(2,1001):
    a = f(a)
    if ndigitos(a.numerator)>ndigitos(a.denominator):
        print a
        c=c+1

print "-----\n",c
