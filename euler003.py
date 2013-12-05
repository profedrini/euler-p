n=600851475143
for k in xrange(3,n,2):
	if n % k == 0 :
		n = n/k
		print k, n
	if n < 2: break
