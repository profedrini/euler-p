def bitlist(n):
    # Returns a list of bits in n 
    # Example  bitlist(n)  -->  [1, 0, 1, 1]
    # Observe it is REVERSED from binary  (13)_2 = 1 1 0 1
    # It is assumed n >= 0
    
    lista = [n & 1]   # Extrae el primer bit
    while n > 1:
        n=n >> 1
        b = n & 1
        lista.append(b)

    return lista

def powermod(a,b,n):
    # Returns a^b  mod n
    if a ==1 : return 1
    if b ==1: return a%n
    a = a%n    
    l = bitlist(b)
    
    factor=a
    potencia = 1
    
    for bit in l:
        if bit ==1:
            potencia = (potencia*factor)%n
        factor = (factor*factor)%n
    
    return potencia

#powermod(5,12,1000)
