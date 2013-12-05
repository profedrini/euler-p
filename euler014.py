# -*- coding: utf-8 -*-
import time
def collatz(n):
    if n<2: return 1
    
    if n%2 == 0 : 
        return n/2
    else:
        return 3*n+1

def serie(m):
    t=1
    L=[m]
    while m >1:
        m = collatz(m)
        L.append(m)    
        t=t+1        
    return L

def problema14(N=10):
    L=[0]*(N+1)    
    L[0]=1
    L[1]=1
    L[2]=2
    # Mata todos los pares
    k=1
    c=1
    while k<N+1:
        L[k]=c
        k=k*2
        c=c+1            
            
    # Mata todos los de la forma 3*2^r
    k=3
    c=8
    while k<N+1:
        L[k]=c
        k=k*2
        c=c+1 

        # Mata todos los de la forma 3*2^r
    k=9
    c=19
    while k<N+1:
        L[k]=c
        k=k*2
        c=c+1     

    for K in range(2,N+1):
        if L[K]==0 :
            m=K
            serie=[m]

            while m > 1:
                #print "collatz(",m,"):",
                m=collatz(m)
                #print m, " ",
                if m<N+1 and L[m]>0: 
                    largo = L[m]
                    for i in range(-1,-len(serie)-1,-1):
                        p = serie[i]
                        largo=largo+1
                        if p < N+1:
                            L[p]=largo
                    break
                else:
                    serie.append(m)
    return L

t=time.time()                                                                                                
S=problema14(2000000)
mx=max(S)
print S.index(mx)
print time.time()-t