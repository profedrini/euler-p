import time
T=time.time()
def sumadigitos2(n):
    return sum(map(int, str(n)))
    

def sumadigitos(n):
    sd=0
    while n >0:
	d = n%10
	sd= sd + d
	n = n/10
	return sd

L = range(2,100)

maxes = []
for k in range(2,101):
    Lk=map(sumadigitos,[m**k for m in L])
    mx = max(Lk)
    i=Lk.index(mx)
    maxes.append( (i,mx))
    # print k, max(Lk)
    
print maxes
print max([m[1] for m in maxes])
print time.time()-T