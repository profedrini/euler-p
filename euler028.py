
side = 1001
a = (side-1)/2
S=1

for n in range(1,a+1):
	d=[(2*n)*(2*n-1)+1 , (2*n)**2 +1, (2*n)*(2*n+1)+1, (2*n+1)**2]
	print d
	S=S+sum(d)

print S
