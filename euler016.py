import time
t=time.time()

print sum( [int(c) for c in str(2**1000)])

print time.time()-t
