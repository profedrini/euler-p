from itertools import *

print [x for x in  islice(permutations(range(10)),10**6-1,10**6)]
