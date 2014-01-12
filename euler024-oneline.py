from itertools import *

print [x for x in  islice(permutations(range(1,10)),2014,2015)]
