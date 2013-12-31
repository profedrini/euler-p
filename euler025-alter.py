from math import log10
from math import sqrt
from math import floor

phi = 1.618033988

a=int(999/log10(phi))
b= int(1000/log10(phi))

for n in range(a,b):
    dF = 1+n*log10(phi)-log10(sqrt(5))
    if dF > 1000:
        print n,int(dF)
        break