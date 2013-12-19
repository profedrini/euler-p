import aritmetica
import math
import time
def generar(l,digits):
	'''genera los numeros con digitos 1,3,7,9 y l cifras en orden creciente'''
	if l==1: return digits
	
	L = []
	for k in range(len(digits)):
		prefix = digits[k]
		suffixes = generar(l-1,digits[k:])
		L.extend( [prefix*10**(l-1)+s for s in suffixes])
	return L


	

def rotar(n):
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
