# -*- coding: utf-8 -*-
'''Problem 125
The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 6^2 + 7^2 + 8^2 +  9^2 + 10^2 + 11^2 + 12^2.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.

Find the sum of all the numbers less than 10^8 that are both palindromic and can be written as the sum of consecutive squares.
'''

'''NOTAS:
Si el mayor número es 10^8 y es suma de al menos dos cuadrados: a^2+b^2 entonces, 
suponiendo a <  b tenemos 2b^2 < 10^8 y por tanto b < 10^4/sqrt(2) < 10^4 / 1.414 < 7073

Por tanto una cota superior es 7073.

Por otro lado

a^2+ (a+1)^2 + ... + (b-1)^2 + (b)^2 = [b(b+1)(2b+1) - (a-1)(a)(2*(a-1)+1]/6
'''
from aritmetica import EsPalindromo
import time
T0=time.time()
L=[]
c=0

SCUADS = [n*(n+1)*(2*n+1)/6 for n in xrange(7074)]

for a in xrange(1,7072):
    for b in xrange(a+1, 7073):
        #suma = (b*(b+1)*(2*b+1)- (a-1)*(a)*(2*(a-1)+1))/6
        suma = SCUADS[b] - SCUADS[a-1]
        if suma>10**8:
            break
        if suma<10**8 and EsPalindromo(suma) :
            L.append(suma)
print sum(set(L))
print time.time()-T0