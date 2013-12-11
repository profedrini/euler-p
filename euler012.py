import time
from primos import ndivisores
import primos
t=time.time()

cota=500
actual = 2  #  n=2 tiene 2 divisor
n=2

while True:
	if n%2 != 0 :  # Si el actual es impar entonces el siguiente es par
		siguiente = ndivisores( (n+1)/2)
	else:
		siguiente = ndivisores(n+1)
	
	numdivisores = actual*siguiente
	if numdivisores>cota:
		print "suma hasta", n, " es igual a", n*(n+1)/2, "y tiene ", numdivisores, "divisores"
		break
	actual = siguiente
	n = n+1

print time.time()-t

print primos.Factorizaciones
