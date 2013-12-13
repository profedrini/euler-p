# -*- coding: utf-8 -*-
def permutaciones(n):
    signs=[-1]*n
    signs[0]=0
    P = range(n) # Inicializa la primera permutacion
    S = dict(zip(P, signs))
    #print "[ ] (     )", P, [S[r] for r in P]    
    nump=1
    while True:
        # Get maximum element with nonzero sign    
        nonzeros= [x for x  in S if S[x] !=0] 
        if len(nonzeros)>0:
            m = max(nonzeros)
        else:
            return nump
        nump = nump+1
        # Swap on its direction
        i = P.index(m)
        j = i+S[m]   # S[i+1] o S[i-1]
        #print "[%d] s(%d, %d)" % (m,i, j),
        P[i], P[j] = P[j], P[i]
        
        # Al llegar al inicio o al final de la lista se hace signo=0
        if j == n-1 or  j == 0:
                S[m]=0
                # print " signo(%d)=0" % m, 
        else: 
            # Si el siguiente en la misma dirección es mayor que el elegido, 
            # también se hace signo cero
            if P[j+S[m]]>P[j]: S[m]=0
        # actualiza los signos
        if m<n:
            for k in range(m+1,n):
                if P.index(k) < j:  # Si k está a la izquierda de m
                    S[k]=+1
                elif P.index(k)>j:  # Si k está a ka derecha de m
                    S[k]=-1
        #print P, [S[r] for r in P]
    return nump
    
import time
import itertools
t = time.time()
for k in xrange(2000):
    print permutaciones(4)
t1 = time.time() - t

t =time.time()
for k in xrange(2000):
    for p in itertools.permutations(range(4)):
        pass # print p
t2 = time.time() - t

print "\n (%f, %f)" % (t1, t2)