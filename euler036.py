L=[]
for n in range(1,10**6):
    decimal = str(n)
    if decimal == decimal[::-1]:
        binario = bin(n)[2:]
        if binario == binario[::-1]:
            print n, decimal, binario
            L.append(n)
            
print sum(L)