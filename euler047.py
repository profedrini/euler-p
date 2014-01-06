from aritmetica import ListaPrimos
from aritmetica import ConjuntoPrimos
from aritmetica import factoriza
from itertools import count

da=factoriza(600)
db = factoriza(601)
dc = factoriza(602)
de = factoriza(603)
e=603
for n in count(604):
    da=db
    db=dc
    dc=de
    de=factoriza(n)
    #print (n, len(da), len(db), len(dc), len(de))
    if len(da)==4 and len(db)==4 and len(dc)==4 and len(de)==4:
        print "\n",(n-3,n-3,n-1,n)
        break
        