#coding=utf8
from itertools import *
from listaprimos import *
import math


Factorizaciones={ p:{p:1} for p in ListaPrimos[:500]}
#Factorizaciones={}

Factoriales=[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000, 2432902008176640000]

def factorial(n):
	if n<0: return 
	if n < len(Factoriales):
		return Factoriales[n]
	else:
		f = Factoriales[-1]
		r = len(Factoriales)
		for k in xrange(r,n+1):
			f=f*k
			Factoriales.append(f)
		return f


        
def factoriza(m):
	n=m

	if n in Factorizaciones: return Factorizaciones[n]
	
	F={}
	
	if n in ConjuntoPrimos:
		F[n]=1 
		Factorizaciones[n]=F
		return F
	
	for p in ListaPrimos:
		if n==1: 	# Si ya tomamos todos los factores, nos detenemos
			Factorizaciones[m]=F
			return F

		if p*p>n:
			# n es primo, no hay necesidad de seguir probando
			F[n]=1
			Factorizaciones[m]=F
			return F

		if n%p==0:
			k=0	
			while n%p == 0 :
				#  p|n, extraemos los factores
				k = k+1
				n = n/p
			F[p]=k


			if n==1: 
				Factorizaciones[m]=F
				return F    # Si no quedan más factores, nos detenemos

			if n in Factorizaciones:
				# Si ya conocemos la factorización de lo que obtuvimos al dividir por p^k
				F.update(Factorizaciones[n])  # fusionamos y terminamos
				Factorizaciones[m]=F
				return F
		

def ndivisores(m):
	if m<1: return 0
	if m==1: return 1

	n=m
	F=factoriza(n)
	r=1
	for k in F:
		r=r*(F[k]+1)
	return r

def sumadivisores(m):
	if m<1: return 0
	if m==1: return 1
	r=1
	F=factoriza(m)
	for p in F:
		r = r*(p**(F[p]+1)-1)/(p-1)
	return r

def sigma(m,k):		
	if m<1: return 0
	if m==1: return 1
	r=1
	F=factoriza(m)
	for p in F:
		r = r*(p**((F[p]+1)*k)-1)/(p**k-1)
	return r


def amigables(a,b):
	sa = sumadivisores(a)-a
	if b == sa:
		sb = sumadivisores(b)-b
		if (a == sb): 
			return True
	
	return False

	
def abundante(n):
	s=sumadivisores(n)-n
	if s>n : 
		return True
	else:
		return False

def perfecto(n):
	s=sumadivisores(n)-n
	if s==n : 
		return True
	else:
		return False
	

def deficiente(n):
	s=sumadivisores(n)-n
	if s<n : 
		return True
	else:
		return False


def GCD(a,b):
	if a == b : return a
	if a ==0 : return b
	if b == 0: return a
	if a==1: return 1
	if b==1: return 1
	return GCD(b,a % b)

def ListGCD(L):
	return reduce(GCD,L)

def LCM(a,b):
	return a*b/mcd(a,b)

def ListLCM(L):
	return reduce(LCM, L,1)


def EsPrimo(n):
    #ConjuntoPrimos=set(ListaPrimos)
    LP = ListaPrimos[-1]
    if (n <= LP):
        if (n in ConjuntoPrimos):
            return True
        else:
            return False
        
    elif (LP<n) and (n<LP*LP):
        # Podemos usar la tabla para calcular rápidamente
        for p in takewhile(lambda x: x*x<=n, ListaPrimos):
            if n%p == 0 : 
                return False
                
        return True
    else:
        print "EsPrimo no es confiable!", LP, n, LP*LP
        return False



def sumadigitos(n):
    sd=0
    while n >0:
	d = n%10
	sd= sd + d
	n = n//10
    return sd


def digitos(n):
    L=[]
    while n >0:
	d=n%10
	L.append(d)
	n=n//10
    return L

def ndigitos(n):
   return int(math.floor(math.log10(n)))+1  # n tiene k cifras
   
def pandigital(dg,k=9, start=1):
    if len(dg)!= k:
        return False
    else:
        if sorted(dg)==range(start,k+1):
            return True
        else:
            return False

def pandigitalstr(s,k=9, start=1):
    if len(s)!=9:
        return False
    else:
        dg = map(int, str(s))
        return pandigital(dg, k,start)
        
def pandigitalgenerator(start=1,end=9,direction=True, string=False):
    digits=range(start, end+1)
    if string:
        digits=map(str,digits)
    if direction==False:
        digits=digits[::-1]

    for p in permutations(digits):
        if string:
            n="".join(p)
        else:
            n=p
        yield n
        
def EsPalindromo(n):
    s=str(n)
    if s == s[::-1]:
        return True
    else:
        return False
        
def totient(n):
    if n<1:
        raise ValueError("Euler's Totient is not defined for zero or negative numbers")
    if n==1: return 1
    if n in ConjuntoPrimos: 
        return n-1
        
    tot=n
    K = factoriza(n)
    for p in K:
        tot = tot*(p-1)/p
    return tot