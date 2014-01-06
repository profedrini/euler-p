k=5
S = 0
for n in xrange(2,1000000):
	digits=[int(c) for c in str(n)]
	suma = sum([a**k for a in digits])
	if n == suma:
		S=S+n
		print n
print "======\n",S
