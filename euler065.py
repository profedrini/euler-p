from fractions import Fraction
from aritmetica import sumadigitos
E = [2,1,2]
for n in xrange(2,40):
    E.extend([1,1,2*n])

for k in range(1,100):
    part = E[:k]
    r=Fraction(1,1)
    #print part[::-1],
    for a in part[::-1]:
        r = a + 1/r 
    print r

print "S:", sumadigitos(r.numerator)