def mcd(a,b):
	if a ==0 : return b
	if b == 0: return a
	if a < b:
		t = a
		a = b
		b = t
		return mcd(a,b)
	else:
		return mcd(b,a % b)

def lcm2(a,b):
	return a*b/mcd(a,b)

def lcm(L):
	return reduce(lcm2, L,1)

A = range(2,20)
print lcm(A)

