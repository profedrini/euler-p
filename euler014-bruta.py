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
        #print m,
        m = collatz(m)
    return t    

t=time.time()
max = 1
start = 1
for m in range(2,1000001):
    l=serie(m)
    if l>max: 
        max = l
        start = m


print max
print start
print time.time()-t