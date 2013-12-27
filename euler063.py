from aritmetica import ndigitos

c=0
for a in xrange(1,50):
    for b in xrange(1,50):
        if ndigitos(pow(a,b))==b:
            print (a,b, pow(a,b))
            c=c+1
            
print "===\n",c
           