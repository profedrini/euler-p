def f(a,b):
    return a*b*(a+1)*(b+1)/4 - 2*10**6
    
MIN = 50000
for a in xrange(1,200):
    for b in range(1,200):
        u=abs(f(a,b))
        if u < MIN:
            print (a,b,a*b,u)
            MIN=u
