#coding=utf8
from aritmetica import pandigitalgenerator
import time
t=time.time()

def check(l):
    primos=[2,3,5,7,11,13,17]
    for k in range(1,8):
        m=l[k]*100+l[k+1]*10+l[k+2]
        if m%primos[k-1] != 0:
            return False
    return True
        
S=0
for s in pandigitalgenerator(start=0):
    if check(s):
        S=S+int("".join(map(str,s)))

print S
#print check( "1406357289")
        
        
print time.time() -t 

