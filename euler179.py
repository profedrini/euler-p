import time
import primos


def cuentadivisores(n):
	if n==1: return 1
	if n<1: return 0


	ndiv = 1
	for p in primos.ListaPrimos:
		c =1 
		while n%p == 0:
			c = c+1
			n = n/p
		ndiv = ndiv*c
	
		if n == 1: return ndiv

		if p*p>n:
			# Si n>1 ya no tiene mas divisores...
			# entonces n es primo y contribuye con p^1
			ndiv = ndiv*2
			break
		if p>n:
			break
	return ndiv


t=time.time()

actual = 2  #  n=2 tiene 2 divisor
n=2
conteo = 0
for n in  xrange(2,10**7):
	#if n%10000==0: print n,"..",
	siguiente = cuentadivisores(n+1)
	if actual ==siguiente: conteo = conteo+1
	actual=siguiente
print "\n======="
print conteo
print cuentadivisores(100)
print cuentadivisores(88)
print cuentadivisores(216)
print time.time()-t
