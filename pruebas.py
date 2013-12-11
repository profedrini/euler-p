from aritmetica import abundante
import time

t=time.time()
top = 28124
abundantes= filter(abundante,xrange(top))

L = range(top)

nab = len(abundantes)
print "hay %d abundantes menores que %d " % (nab,top)

for i in range(nab):
	r = abundantes[i]
	for j in range(i,nab):
		s=abundantes[j]
		#print (r,s)
		if r+s<top:
			if L[r+s]>0:
				L[r+s]=0
		else:
			break

print sum(L)
print time.time()-t,"segundos"
