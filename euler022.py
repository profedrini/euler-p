# -*- coding: utf8 -*-

def valor(s):
	'''regresa el valor obtenido al sumar los valores
	correspondientes a la posición alfabética de cada letra'''

	return sum([ord(c)-64 for c in s])

f = open("names.txt", "r")
NAMES=f.read().replace('"',"").split(",")

f.close()
NAMES.sort()
r = len(NAMES)

print sum([valor(NAMES[k])*(k+1) for k in range(r)])
	
