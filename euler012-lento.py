import time

def factoriza(n):
    F={}
    
    if n==1: return {1:0}
    
    c=0
    while n%2 == 0 :
        c = c+1
        n  = n/2
    else:
        if c > 0: F[2]=c
 
    for p in range(3,n+1,2):
        c = 0
        while n%p == 0 :
            c = c+1
            n  = n/p
        else:
            if c > 0: F[p]=c
	
	if p>n and n>1:
		F[n]=1
		break
        
    return F
   

def factorizaGauss(m):
	F={}
	Fm = factoriza(m)
	Fn = factoriza(m+1)
	for x in Fm:
		F[x] = Fm[x]

	for y in Fn:
		F[y]=Fn[y]
	
	F[2]=F[2]-1
	return F


def CuentaDivisoresGauss(n):
	if n<1: return 0
	if n==1: return 1
	F=factorizaGauss(n)
	p=1
	for x in F:
		p = p*(F[x]+1)

	return p
    
t=time.time()

for k in range(2,100000):
	cd = CuentaDivisoresGauss(k)
	if cd>500: 
		g = k*(k+1)/2
		print k, cd,g
		break

print time.time()-t
