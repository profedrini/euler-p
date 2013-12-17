import aritmetica
import math
import time

def rotar(n):
    #print "n:", n
    k = int(math.floor(math.log10(n)))  # n tiene k cifras
    for i in range(k+1):
        if (not aritmetica.EsPrimo(n)):
            return False
        d = n%10
        n = (n - d)//10 + 10**k*d
    return True
        
            
t=time.time()  
L=[]
for n in range(2,10**6):
    if rotar(n): L.append(n)

print L
c=len(set(L))
print c
print time.time()-t