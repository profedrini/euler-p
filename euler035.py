def rotate(
def generar(l,digits):
	'''genera los numeros con digitos 1,3,7,9 y l cifras en orden creciente'''
	if l==1: return digits
	
	L = []
	for k in range(len(digits)):
		prefix = digits[k]
		suffixes = generar(l-1,digits[k:])
		L.extend( [prefix*10**(l-1)+s for s in suffixes])
	return L


print generar(3,[1,3,7,9])
	
