#! /usr/bin/python

import sys

# This function converts numbers into phrases. Example: 105 -> onehundred and five
def convert(n):
	token0to19 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	token20to90 = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	token100to900 = ['onehundred', 'twohundred', 'threehundred', 'fourhundred', 'fivehundred', 'sixhundred', 'sevehundred', 'eighthundred', 'ninehundred']
	token1000 = 'onethousand'
	strNum = str(n)	# 578 -> '578'
	size = len(strNum)
	num = []
	phrase = ''
	
	for i in range(0, size): # '578' -> ['5', '7', '8']
		num.append(strNum[i])
		
	if size == 4:
		phrase += token1000;
	elif size == 3:
		phrase += token100to900[int(num[0]) - 1]
		if num[1] != '0' or num[2] != '0':
			phrase += 'and'
		if num[1] == '0' and num[2] != '0':									# ex.) 105
			phrase += token0to19[int(num[2])]
		elif num[1] != '0' and num[2] == '0' and int(num[1]) < 2: 	# ex.) 110
			phrase += token0to19[int(num[1]) + 9]
		else: 																		# ex.) 115
			if int(num[1]) >= 2:
				phrase += token20to90[int(num[1]) - 2] + token0to19[int(num[2])]
			else:
				phrase += token0to19[int(num[1] + num[2])]
	elif size == 2 and n >= 20:
		phrase += token20to90[int(num[0]) - 2] + token0to19[int(num[1])]		
	else:
		phrase = token0to19[n]
	
	return phrase

# Main
cnt = 0
for i in range(1, int(sys.argv[1]) + 1):
	cnt += len(convert(i))
print cnt

