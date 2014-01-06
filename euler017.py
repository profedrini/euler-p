digits = ["one", "two", "three", "four", "five", "six","seven", "eight", "nine"]

tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tenprefixes = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

hundredprefixes= ["onehundred","twohundred","threehundred","fourhundred","fivehundred","sixhundred","sevenhundred","eighthundred","ninehundred"]


sumdigits = sum(map(len, digits))

sumtens = sum(map(len, tens))

for p in tenprefixes:
	print p,
	sumtens = sumtens + len(p)*10 +sumdigits
	print sumtens + sumdigits

sumdigitsandtens = sumdigits + sumtens

sumhundreds=0	
for h in hundredprefixes:
	sumhundreds=sumhundreds+len(h) + (len(h)+3)*99 + sumdigitsandtens
	

suma=sumdigitsandtens+sumhundreds
print suma + len("onethousand")



