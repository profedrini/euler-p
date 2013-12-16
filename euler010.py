import math
import time

t1 = time.time()

N=2000001
L = [1]*N
P = []
S=0
L[0]=0
L[1]=0

for m in xrange(N):
	if L[m] !=0:
		L[m]=m
		#P.append(m)
		for k in xrange(2,int((N+1)/m)+1):
			if m*k < N:
				L[m*k]=0

'''S=0
for k in range(N-1):
	if L[k]==True:
		# L[k]=k
		S =S+k
'''
S=sum(L)
print(S)
t2=  time.time()

print(t2-t1)
		
