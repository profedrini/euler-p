'''Problem 62
The cube, 41063625 (345^3), can be permuted to produce two other cubes:
    56623104 (384^3) and 66430125 (405^3). 
    In fact, 41063625 is the smallest cube which has exactly three permutations 
    of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''
import time
from aritmetica import digitos
from itertools import permutations
print "precalculando..."

CUBOS = {n**3 for n in range(10**5)}
T1=time.time()
D={}

for n in xrange(10**5):
    digs=tuple(sorted(digitos))
    
def l2i(L):
    l=L[::-1]
    return     sum( [a*10**(k) for (k,a) in enumerate(l)])

def next_permutation(seq, pred=cmp):
    """Like C++ std::next_permutation() but implemented as
    generator. Yields copies of seq."""

    def reverse(seq, start, end):
        # seq = seq[:start] + reversed(seq[start:end]) + \
        #       seq[end:]
        end -= 1
        if end <= start:
            return
        while True:
            seq[start], seq[end] = seq[end], seq[start]
            if start == end or start+1 == end:
                return
            start += 1
            end -= 1
    
    if not seq:
        raise StopIteration

    try:
        seq[0]
    except TypeError:
        raise TypeError("seq must allow random access.")

    first = 0
    last = len(seq)
    seq = seq[:]

    # Yield input sequence as the STL version is often
    # used inside do {} while.
    yield seq
    
    if last == 1:
        raise StopIteration

    while True:
        next = last - 1

        while True:
            # Step 1.
            next1 = next
            next -= 1
            
            if pred(seq[next], seq[next1]) < 0:
                # Step 2.
                mid = last - 1
                while not (pred(seq[next], seq[mid]) < 0):
                    mid -= 1
                seq[next], seq[mid] = seq[mid], seq[next]
                
                # Step 3.
                reverse(seq, next1, last)

                # Change to yield references to get rid of
                # (at worst) |seq|! copy operations.
                yield seq[:]
                break
            if next == first:
                raise StopIteration
    return
    
def permuta3(m):
    C=[]
    for p in next_permutation(sorted(digitos(m))):
        k=l2i(p)
        if k in CUBOS:
            C.append(k)
            
    return set(C)
    
for n in range(10,5000):
    v=permuta3(n**3)
    if len(v)>2:
        print n, len(v), time.time()-T1