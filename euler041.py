# -*- coding: utf-8 -*-
from itertools import *
from aritmetica import *

digits = ["9", "8","7", "6","5","4","3","2","1"]

stop=False
for k in range(9,2,-1):
    for p in permutations(digits[-k:],k): 
        n = int("".join(p))
        if EsPrimo(n): 
            print n
            stop=True
            break
    if stop: break
    