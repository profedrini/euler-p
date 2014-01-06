# -*- coding: utf-8 -*-
from operator import truediv
from fractions import Fraction
def Resuelve(A):
    '''Resuelve el sistema de ecuaciones dado por la matriz A que es una matriz
    de n x (n+1) , la ultima columa siendo el vector de términos independientes'''
    n=len(A)    
    for i in range(n):
        if A[i][i] == 0:
            # Se necesita hacer un pivoteo en fila i, cambiar la fila por otra que esté abajo"
            for r in range(i+1, n):
                if A[r][i] != 0:
                    #print "intercambiaria fila", i, "con", r
    
                    v= A[r]
                    A[r] = A[i]             #Ponemos la fila de arriba en la de abajo
                    A[i]= v                 #Arriba ponemos lo que habíamos guardado
    
    
        for k in range(n):
            if k!=i:
                M = Fraction(A[k][i],A[i][i])
    
                for j in range(n+1):
                    A[k][j] = A[k][j] - M*A[i][j]
    

    sols=[]
    for m in range(n):
        a=A[m][-1]
        b=A[m][m]
    
        x=truediv(a,b)
        x=Fraction(a,b)
    
        sols.append(x)
    return sols
    


def Interpola(L):
    print "interpolando", L
    m=len(L) 
    A=[]
    for i in range(m):
        V=[]

        for k in range(m):
            a = ( (L[i][0])**(m-k-1) )
            V.append(a)
        V.append(L[i][1])
        A.append(V)
        #print A
        
    #print "MATRIZ"
    #for l in A: print l
    #print "SOLUCIONES"
    sols=Resuelve(A)
    #print sols
    return sols
    
def Evalua(coef,x):
    m=len(coef)
    p=sum(coef[k]*x**(m-k-1) for k in range(len(coef)))
    #print "evaluando en", x, "= ",p 
    return p

    
def u(n):
    return sum( [(-n)**k for k in range(11)])
    

S=0   
for m in range(10):
    L=[ (k+1,u(k+1)) for k in range(m+1)]
    print L, "\n\t",
    s = Interpola(L)
    y = Evalua(s, k+2)
    print y
    S=S+y
print "===="
print S