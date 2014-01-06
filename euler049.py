from aritmetica import *

def de4cifras(p):
    if p>1000 and p <10000:
        return True
    else:
        return False

P4 = filter(de4cifras,ListaPrimos)

Nprimos=len(P4)

for a in range(Nprimos-2):
    for b in range(a+1,Nprimos-1):
        if sorted(digitos(P4[a]))==sorted(digitos(P4[b])):
            for c in range(b+1, Nprimos):
                if P4[c] + P4[a] == 2*P4[b]:
                    if sorted(digitos(P4[b]))==sorted(digitos(P4[c])):
                        print (P4[a],P4[b],P4[c])
                        
