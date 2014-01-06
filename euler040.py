from itertools import *
from aritmetica import *
import time

T=time.time()
def chaper(top):
    k = 0
    for n in count(1):
        dg = digitos(n)[::-1]
        
        for d in dg:
            k = k+1
            yield (k,d)
            
        if n>top: return
        

p=1
picks={10**x for x in range(8)}
print picks                
for d in chaper(10**6):
    if d[0] in picks : 
        p=p*d[1]
        print d,
        
print "\n",p            
print time.time()-T