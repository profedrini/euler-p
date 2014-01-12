# -*- coding: utf-8 -*-
'''Problem 70
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.'''

from __future__ import division

from aritmetica import factoriza
from aritmetica import totient
from aritmetica import ndigitos
from aritmetica import digitos
import aritmetica
import time

Tt=time.time()

MIN=1.1
for n in xrange(2,10**7):
    t = totient(n)
    #print n, t
    if (ndigitos(t) == ndigitos(n)) and (n/t<MIN) and (sorted(digitos(t))==sorted(digitos(n))):
        print n, t, n/t
        MIN=n/t
                    
print "\n====\n", time.time()-Tt