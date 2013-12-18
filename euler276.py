#coding=utf8
import time
import aritmetica
from aritmetica import ListGCD
from aritmetica import GCD
t= time.time()
S=0
top = 12

for a in xrange(1,top/3+1):
	for b in xrange(a,top/2):
		g = GCD(a,b)
		if g == 1 	:
			k=min(a+b,top/2, top-a-b)-b
			S=S+k
			print "[[%d, %d]] " % (a,b), k,  (a+b-b, top/2-b, top-a-b-b)
		for c in xrange(b, min(a+b, top/2,top-a-b)):
				h = GCD(g,c)
				if h==1:
					S=S+1
					print (a,b,c)
print S
