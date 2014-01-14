from geometria import ProductoCruz as Cruz
L=[(-340,495),(-153,-910),(835,-947)]


def sign(x):
	if x > 0:
		return 1
	elif x<0:
		return -1
	else:
		return 0

cuenta=0
with open("triangles.txt", "r") as source:
	for line in source:
		P= map(int,line.split(","))
		L=[[P[0],P[1],0],[P[2],P[3],0],[P[4],P[5],0]]
		S=0
		for k in range(-1,2):
			z=Cruz(L[k],L[k+1])
			S=S+sign(z[2])
			if S ==3 or S ==-3: cuenta = cuenta+1

print cuenta
