#coding=utf8
from aritmetica import factorial

def cabe(a, n=10):
	'''determina cual es el mayor factorial menor a n! que 
		quepa en el número a, cuántas veces cabe y cual es el residuo'''

	t=0
	for k in range(n):
		if factorial(k)<= a: 
			t=k
		else:
			break

	#  t es el máximo tal que  t! \leq a
	f = factorial(t)
	
	return (a,t, (a-1)/f, a%f)


a=1000000
digits = [0,1,2,3,4,5,6,7,8,9]
permutacion=[]
while a>=0:
	x = cabe(a,10)
	print x, "removing pos %d = %d from " % (x[2], digits[x[2]]), digits,
	d = digits.pop(x[2])
	print "sobra", digits
	permutacion.append(d)
	if len(digits)<1 : break	
	a = x[3]
permutacion=permutacion+digits
print permutacion
