# -*- coding: utf-8 -*-
from itertools import tee
from itertools import izip
from itertools import imap

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)
    
def quantify(iterable, pred=bool):
    "Count how many times the predicate is true"
    return sum(imap(pred, iterable))
    

row=[0,1,2,1,0]

print quantify(row, lambda x: x>3)

S=0
for n in xrange(3,101):
    row=[0]+[sum(p) for p in pairwise(row)]+[0]
    
    a = quantify(row, lambda x: x>10**6)
    print a
    S=S+a

print S
