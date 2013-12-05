import time
def collatz(n):
    if n<2: return 0
    
    if n%2 == 0 : 
        return n/2
    else:
        return 3*n+1

def serie(m):
    t=1
    while m >1:
        t=t+1
        print m,
        m = collatz(m)
    print 
    return t    


print serie(7)