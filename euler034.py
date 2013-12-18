Factorials=[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
S=0
for n in range(3,1000000):
	s = sum( [Factorials[k] for k in map(int, str(n))])
	if s==n:
		S=S+n
		print n

print "\n\n",S

