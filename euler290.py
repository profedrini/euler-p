from aritmetica import sumadigitos
import time
T0=time.time()
c=0
for n in xrange(9,10**18,9):
    if sumadigitos(n) == sumadigitos(137*n):
        c+=1
        
print c
print time.time()-T0
        