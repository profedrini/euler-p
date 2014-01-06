NUMS = range(13)
SUITS = "HSCD"

def Canoniza(hand):
    for card in hand:
        if card[0]=="T": card[0]="10"
        if card[0]=="J": card[0]="11"
        if card[0]=="Q": card[0]="12"
        if card[0]=="K": card[0]="13"
        if card[0]=="A": card[0]="14"
        card[0] = int(card[0])-2
    return hand

def Separa(ab):
    return [ab[0],ab[1]]
    
def ParseLine(l):
    L=map(Separa,l.split())
    first = L[:5]
    second = L[5:]
    return (first, second)      
                        
def DoCounts(hand):
    handnums = [c[0] for c in hand]
    counts = range(13)
    for n in range(13):
        counts[n] = handnums.count(n)
    return counts 

def IsPair(counts):
    if counts.count(2)==1:
        return True
    else:
        False
        
def IsTwoPairs(counts):
    if counts.count(2)==2:
        return True
    else:
        False

def IsThree(counts):
    if counts.count(2)==1:
        return True
    else:
        False

def IsStraight():
    # FIX
    return 
    
def IsFlush(hand):
    handsuits = [c[1] for c in hand]
    for s in SUITS:
        if handsuits.count(s) == 5:
            return True
    return False


def FullHouse(counts):
    return  IsThree(counts) and IsPair(counts)
    
def IsPoker(counts):
    if 4 in counts:
        return True
    else:
        return False

def IsStraightFlush(hand):
    return IsStraight(counts) and IsFlush(hand)            

def HighCard(hand):

def FightToDeath(hand1, hand2):
                
match=ParseLine("6S 8D 4C 8S 6C QH TC 6D 7D 9D")
v=Canoniza(match[0])
print DoCounts(v)
print v