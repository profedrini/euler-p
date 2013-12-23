from aritmetica import *

def check(n):
    s=str(n)
    k=1
    while len(s)<9 and k<10:
        k=k+1
        m = n*k
        s=s+str(m)
        if pandigitalstr(s):
            print (n,s)
            return (True,int(s))

    return (False,0)

max=192384576

for n in xrange(185, 99999):
    u,m=check(n)
    if u and m>max:
        max = m
        print n

