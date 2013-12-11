import drini
m = 10**10
s=0
for k in xrange(1,1001):
	s = (s + drini.powermod(k,k,m))%m

print s
