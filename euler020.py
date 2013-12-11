p=1
for k in xrange(2,101):
	p=p*k

print sum(map(int,str(p)))
