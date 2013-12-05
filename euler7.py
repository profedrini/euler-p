import math
import time


t1 = time.time()

N=200000
L = [True]*N
P = []
S=0
L[0]=False
L[1]=False

for m in range(N):
	if L[m] == True:
		#P.append(m)
		for k in range(2,int((N+1)/m)+1):
			if m*k < N:
				L[m*k]=False

c=0
for k in range(N-1):
	if L[k]==True:
		L[k]=k
		c=c+1
		if c == 10001:
			print k
			break



#print(sum(P))
#print(S)
t2=  time.time()

print(t2-t1)
#print(L)
		
