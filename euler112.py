'''Problem 112
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
'''
from aritmetica import digitos
from itertools import tee
from itertools import izip
from itertools import count
from operator import truediv

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

def signo(n):
    if n>0: 
        return 1
    elif n<0:
        return -1
    else:
        return 0
        
def Bouncy(n):
    l = digitos(n)
    if len(l)<3: return False
    
    SG=map(signo,[par[1]-par[0]  for par  in pairwise(l)])
    #print SG
    
    if 1 in SG and -1 in SG:
        return True
    else:
        return False
    
b = 0
reach50 = False
reach90 = False
reach99 = False

for n in count(1):
    if Bouncy(n): b = b+1
    #if n%100 == 0: print n,b,truediv(b,n)
    if not(reach50) and b >= 0.5*n:
        reach50 = True
        print "alcanzamos 50%", n
        continue
        
    if not(reach90) and b >= 0.9*n:
        reach90 = True
        print "alcanzamos 90%", n
        continue
        
    if not(reach99) and b >= 0.99*n:
        reach99 = True
        print "alcanzamos 50%", n
        break
        