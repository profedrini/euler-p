import time
T0=time.time()
a=0
b=1
m=1

while(b<10**999):
	c = a+b
	a,b = b,c
	m=m+1

print b
print m

print time.time()-T0