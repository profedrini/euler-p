from itertools import ifilter
from itertools import imap

def EsPalindromo(s):
    if s == s[::-1]:
        return True
    else:
        return False
        
        
def itera(s):
    return str(int(s) + int(s[::-1]))
    
    
def Lychrel(s):
    s=itera(s)
    for n in xrange(57):
        if EsPalindromo(s): 
            return False
        s=itera(s)
    
    return True

S=0
for s in imap(str, xrange(10**4)):
    if Lychrel(s): 
        #print s
        S=S+1
    
print S