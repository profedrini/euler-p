'''Problem 76
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
'''
from aritmetica import sumadivisores

P=[1,1,2,3,5,7,11]

for n in xrange(7,101):
    p = sum([sumadivisores(n-k)*P[k] for k in range(n)])/n
    #print n, ": sumando", [((n-k,k),(ndivisores(n-k),P[k])) for k in range(n)]
    P.append(p)

print P[100]