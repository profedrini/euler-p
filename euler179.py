import time
from primos import ndivisores

t=time.time()

actual = 2  #  n=2 tiene 2 divisor
n=2
conteo = 0
for n in  xrange(2,10**7):
	siguiente = ndivisores(n+1)
	if actual ==siguiente: conteo = conteo+1
	actual=siguiente
print "\n======="
print conteo
print time.time()-t

