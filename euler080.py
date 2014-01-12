from aritmetica import *
from math import *

def sraiz(c):
    S=0
    p=0
    for i in xrange(100):
        x=0
        while x*(20*p+x)<=c:
            x=x+1
        x=x-1
        y = x*(20*p+x)
        S=S+x
        c=100*(c-y)
        p=10*p+x
    return S


S = 0
squares = {x*x for x in range(10)}

for x in xrange(2,100):
    if x not in squares:
        S=S+sraiz(x)
        
print S