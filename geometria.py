import itertools

def ProductoCruz(u,v):
	return (u[1]*v[2]-v[1]*u[2], u[2]*v[0]-v[2]*u[0], u[0]*v[1] - v[0]*u[1])

def ProductoPunto(u,v):
	sum(imap(operator.mul, u,v))
