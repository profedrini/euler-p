'''A particular school offers cash rewards to children with good attendance and punctuality. If they are absent for three consecutive days or late on more than one occasion then they forfeit their prize.

During an n-day period a trinary string is formed for each child consisting of L's (late), O's (on time), and A's (absent).

Although there are eighty-one trinary strings for a 4-day period that can be formed, exactly forty-three strings would lead to a prize:

OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
LAOO LAOA LAAO

How many "prize" strings exist over a 30-day period?'''

'''If  T(n) represents the nth tribonacci number starting with [1,2,4] for n=0,1,2
and if P(n) is the number of prize strings for n days, then

P(n) = T(n-1) + P(n-1) + T(n-2)+P(n-2)+ T(n-3)+P(n-3) = T(n) + P(n-1) + P(n-2)+P(n-3)'''


TRIBOS=[1,2,4,7]
for n in range(4,35):
    TRIBOS.append(sum(TRIBOS[-3:]))

P=[0,3,8,19,43]
for n in range(5,35):
    P.append(sum(P[-3:])+TRIBOS[n])

print P
print P[4]
print P[30]