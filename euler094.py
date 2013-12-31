# -*- coding: utf-8 -*-
'''It is easily proved that no equilateral triangle exists with integral 
length sides and integral area. However, the almost equilateral triangle 5-5-6
has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle
for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with 
integral side lengths and area and whose perimeters do not exceed1,000,000,000.'''

'''NOTAS:
1) ===========
Aplicando la fórmula de herón con lados (a,a,b) obtenemos que S^2 es igual a 

b^2(2a+b)(2a-b) / 16
lo cual solo puede ser entero si b es par

Como a,b son consecutivos, esto quiere decir que a es impar.

2) ================
Además, para que sea cuadrado perfecto, (2a+b)(2a-b) debe ser cuadrado, es decir
4a^2 - b^2 = c^2
esto es...

b^2 + c^2 = (2a)^2

3) ====================
Sustituimos ahora, b = 2k,   a = 2k+-1 y tenemos dos expresiones que deben ser cuadrados:
    4(3k+1)(k+1)   (a,a,b)
    4(3k-1)(k-1)   (b,a,a)
de las cuales podemos hacer caso omiso del 4

4) ===============
Como a=b+-1 y el perimetro no excede 10^9, entonces a recorre hasta  10^9/3.
por tanto k recorre hasta  10^9/6
'''
import time
from math import floor
from math import sqrt
T0 = time.time()

Cuadrados = {n*n for n in xrange(10**7)}

print "Precálculo de cuadrados:", time.time() - T0

def EsCuadrado(m):
    if m<10**14:
        if m in Cuadrados:
            return True
        else:
            return False    

    if m%3 == 2: return False
    if m%8 not in {0,1,4} : return False
    if m%10 not in {0,1,4,5,6,9} : return False
    
    v=sqrt(m)
    if v-floor(v)>0:
        return False
    else:
        return True

def Verify(a,b):
    '''a = 3k+1 or 3k-1
       b = k+1 or k-1
       
       Since gcd(a,b)=1,2'''
    if a%2 ==1 or b%2 ==1:
        # En este caso ambos deben ser primos relativos, por tanto ambos cuadrados
        if ((a%10)*(b%10))%10 not in  {0,1,4,5,6,9} : return False

        if EsCuadrado(a) and EsCuadrado(b):
            return True
        else:
            return False
    else: # Ambos pares
        return Verify(a/2, b/2)

T1=time.time()
print "inicia revisión",T1-T0
c=0
S=0
for k in xrange(1,10**9/3):
    if 2*(2*k-1)+2*k>10**9: break
    if Verify(3*k-1, k-1):
        c=c+1
        print k,  k-1, 3*k-1,  ((2*k-1), 2*k), "\tt:", time.time()-T1, c
        S=S+2*(2*k-1)+2*k
    elif Verify(3*k+1, k+1):
        c=c+1
        print k,k+1, 3*k+1,  ((2*k+1),2*k), "\tt:", time.time()-T1, c
        S=S+2*(2*k+1)+2*k
print "matches:",c
print "suma de perímetros", S
print "total time:",time.time()-T0