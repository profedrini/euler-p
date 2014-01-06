'''Problem 99
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.'''

from math import log

L=[]
nline=0
with open('base_exp.txt') as f:
    for line in f:
        nline+=1
        par = map(int, line.split(","))
        lg = par[1]*log(par[0])
        L.append((nline,par[0],par[1], lg))
L.sort(key=lambda u: u[3])
print L[-5:]