#coding=utf8
import itertools
import operator
from itertools import imap

'''Este programa cuenta el numero de ternas pitagóricas cuyo suma es menor o igual a 10 millones'''

import time

t1 = time.time()

TP = [(3,4,5)]
perim = 10**7 
c=0

def dot(v1,v2):
	return sum(imap(operator.mul, v1,v2))


while len(TP)>0:
	t = TP.pop()
	c=c+1
	terna1 = ( -t[0]+2*t[1]+2*t[2], -2*t[0]+t[1]+2*t[2], -2*t[0]+2*t[1]+3*t[2])
	terna2 = (  t[0]+2*t[1]+2*t[2],  2*t[0]+t[1]+2*t[2],  2*t[0]+2*t[1]+3*t[2])
	terna3 = (  t[0]-2*t[1]+2*t[2],  2*t[0]-t[1]+2*t[2],  2*t[0]-2*t[1]+3*t[2])
	nuevas= [terna for terna in [terna1,terna2,terna3] if sum(terna)<= perim ]
	TP.extend(nuevas)

print c
print time.time() - t1
