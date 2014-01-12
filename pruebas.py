#coding=utf8
from aritmetica import *
import time
t=time.time()

def check(s):
    primos=[2,3,5,7,11,13,17]
    for k in range(1,8):
        m=int(s[k:k+3])
        #print "testing %d mod(  %d) = %d" % (m,primos[k-1],m%primos[k-1]),k
        if m%primos[k-1] != 0:
            return False
    return True
        
S=0
for s in pandigitalgenerator(direction=False,start=0,string=True):
    if check(s):
        S=S+int(s)
        print s

print S
#print check( "1406357289")
        
        
print time.time() -t 

