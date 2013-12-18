import math

def findcycle(d):
	'''encuentra la longitud del ciclo de 1/d'''
	dec = 0
	x = 1
	C = []
	while True:
		q = 10*x//d
		r = (10*x)%d
		if r==0: 
			return 0
		elif (q,r) in C  :
			oldec = C.index( (q,r) )
			return dec-oldec
		else:
			dec = dec+1
			C.append((q,r))
			x = r

max = 1
n = 3	
for d in xrange(1,1000):
	k = findcycle(d)
	if k > max:
		n=d
		max = k
		print "[[%d, %d]]" %(d,findcycle(d))
