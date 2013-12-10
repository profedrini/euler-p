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
		if p>n:
			break
	return ndiv


t=time.time()

cota=500
actual = 2  #  n=2 tiene 2 divisor
n=2

while True:
	if n%2 != 0 :  # Si el actual es impar entonces el siguiente es par
		siguiente = cuentadivisores( (n+1)/2)
	else:
		siguiente = cuentadivisores(n+1)
	
	numdivisores = actual*siguiente
	if numdivisores>cota:
		print "suma hasta", n, " es igual a", n*(n+1)/2, "y tiene ", numdivisores, "divisores"
		break
	actual = siguiente
	n = n+1

print time.time()-t
