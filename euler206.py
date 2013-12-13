import time

def matches(s):
    if len(s) != 17:
        return False
    else:
        if s[0]=="1" and s[2] == "2" and s[4] == "3" and s[6] == "4" and s[8] == "5" and s[10] == "6" and s[12] == "7" and s[14] == "8" :
            return True

t=time.time()

n = 10**7
a=n+3
b=n+7
a2 = a*a
b2 = b*b
while a < 139*(10**6):
    a2 = a*a
    sa = str(a2)
    if matches(sa):
        print "answer: %d, square: %d"% (a*10,a2*100)
        break
    a=a+10
    
    b2=b*b
    sb =str(b2)
    if matches(sb):
        print "answer: %d, square: %d"% (b*10,b2*100)
        break
    b = b+10
    
print time.time()-t , "segundos"