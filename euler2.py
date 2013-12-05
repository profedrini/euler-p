# -*- coding: utf-8 -*-
#  1, 1, [2], 3, 5, [8], 13, 21, [34], 55, 89, [144]
# Hay que sumar las posiciones congruentes a 3 modulo 4.
#  f(n+1) = f(n) + f(n-1)
#  f(n+2) = f(n+1) + f(n) = 2f(n) + f(n-1)
#  f(n+3) = f(n+2) + f(n+1) = 2f(n) + f(n-1) + f(n)+f(n-1) = 3f(n)+2f(n-1)

a = 1
b = 2
suma = 2    # Al inicio  f(1) = 1, f(2) = 2, como si a fuese n-1,  b fuese n
print suma
while( True):

    a, b = (2*b+a), (3*b + 2*a)
    if b >= 4000000:
        break
    else:
        suma = suma + b  # Avanzamos tres posiciones y sumamos
        print "añadiendo",b,suma