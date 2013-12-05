def IsCapicua(n):
    if n<100000 : return False
    k = n/100000
    r = n % 10 
    if k != r:
        return False
    else:
        n = (n-k*100000-r) / 10
        k = n / 1000
        r = n% 10
        if k!=r:
            return False
        else:
            return True


A = range(990,100,-11)
B = range(999,100,-1)


L=filter(IsCapicua,[a*b for a in A for b in B])

L = list(set(L))
L.sort()

print L[-1]
