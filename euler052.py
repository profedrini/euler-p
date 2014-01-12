import aritmetica
import itertools
import time

T=time.time()

def check(n):
    '''checks if n,  kn have the same digits'''
    L=aritmetica.digitos(n)

    for k in range(2,7):    
        Lk=aritmetica.digitos(n*k)   
        if sorted(L)!= sorted(Lk):
            return False
    return True
    
for n in itertools.count(1):
    if check(n):
        print [n*k for k in range(1,7)]
        break
        
print time.time()-T