from aritmetica import ListaPrimos as P

def check(n):
	m = n-1
	return  (pow(P[m]-1,m+1,P[m]**2)+pow(P[m]+1,m+1,P[m]**2))%(P[m]**2)

for n in xrange(7037,len(P)):
	if check(n)>10**10:
		print n
		break
