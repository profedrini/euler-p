#coding=utf8

'''Este programa cuenta el numero de ternas pitagóricas cuyo suma es menor o igual a 10 millones'''

import time

t1 = time.time()

TP = [[3,4,5]]
perim = 10**3 +1
c=0
sumas={k:0 for k in xrange(1001)}


while len(TP)>0:
	t = TP.pop()
	T=t[:]
	r=1
	print T, ": ",
	while sum(T)<= perim:
            print T
            s=sum(T)
            sumas[s]=sumas[s]+1
            r=r+1
            T[0],T[1],T[2] = r*t[0],r*t[1],r*t[2]
	    
	
	terna1 = [ -t[0]+2*t[1]+2*t[2], -2*t[0]+t[1]+2*t[2], -2*t[0]+2*t[1]+3*t[2]]
	terna2 = [  t[0]+2*t[1]+2*t[2],  2*t[0]+t[1]+2*t[2],  2*t[0]+2*t[1]+3*t[2]]
	terna3 = [  t[0]-2*t[1]+2*t[2],  2*t[0]-t[1]+2*t[2],  2*t[0]-2*t[1]+3*t[2]]
	nuevas= [terna for terna in [terna1,terna2,terna3] if sum(terna)<= perim ]
	TP.extend(nuevas)

mx = max(sumas.values())
n=0
for k,v in sumas.iteritems():
	if v == mx:
		print (n,v)
		break
print time.time() - t1
