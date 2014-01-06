from aritmetica import amigables
from aritmetica import sumadivisores
import time

t=time.time()
s=0
top = 10000

for a in xrange(2,top):
	sa = sumadivisores(a)-a
	if sa > a:
		b = sumadivisores(sa)-sa
		if a == b:
			print (a,sa,b)
			if sa<top:
				s=s+a+sa

print s

print time.time()-t
