import time
t = time.time()
entrada = open("triangle.txt","r")
D=[]
for l in entrada:
	D.append(map(int,l.split()))
entrada.close()

nrows= len(D)

for r in range(nrows-2,-1,-1):
	# Vamos a procesar la fila "r"
	#print "recorriendo", D[r]
	for k in range(len(D[r])):
		D[r][k] = D[r][k] + max(D[r+1][k] , D[r+1][k+1])

print D[0][0]
print time.time()-t , "segundos"
