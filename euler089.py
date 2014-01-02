# -*- coding: utf-8 -*-
'''
The rules for writing Roman numerals allow for many ways of writing each number (see About Roman Numerals...). However, there is always a "best" way of writing a particular number.

For example, the following represent all of the legitimate ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

The last example being considered the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; that is, they are arranged in descending units and obey the subtractive pair rule (see About Roman Numerals... for the definitive rules for this problem).

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
'''

def reduce(s):
    
    if "DCCCC" in s:
        s = s.replace("DCCCC", "CM")
    if "CCCC" in s:
        s = s.replace("CCCC", "CD")
    if 'LXXXX' in s:
        s = s.replace('LXXXX','XC')
    if 'XXXX' in s:
        s = s.replace('XXXX','XL')
    if 'VIIII' in s:
        s = s.replace('VIIII','IX')
    if 'IIII' in s:
        s = s.replace('IIII','IV')        

    return s
    
size0=0
size1=0
with open('roman.txt') as f:
    for s in f:
        size0 = size0 + len(s) # Llevamos la cuenta del tamaño original
        snew = reduce(s)
        size1 = size1 + len(snew)
        
print size1-size0        