from fractions import Fraction
import time
T0=time.time()
maxd = 8
maxf = Fraction(0,1)
f37 = Fraction(3,7)

for d in range(2,10**6+1):
    a = int(3*d/7)
    r = Fraction(a,d)
    if maxf < r and r < f37:
        maxf = r
        
print maxf
print time.time()-T0