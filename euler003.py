from aritmetica import ListaPrimos
n=600851475143
for k in ListaPrimos:
	if n % k == 0 :
		while (n%k==0):
			n = n/k
		print k
	if n < 2: break
