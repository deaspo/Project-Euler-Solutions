def sigma2(number):
	"""
	Returns the sum of all squared divisors of number
	"""
	from pe_math import get_divisors
	sum = 0
	for divisor in get_divisors(number):
		sum += divisor * divisor

	return sum

def SIGMA2(number):
	i = 1
	sum = 0
	while i <= number:
		sum += sigma2(i)
		i += 1

	return sum

if __name__ == "__main__":
	"""
	The divisors of 6 are 1,2,3 and 6.
	The sum of the squares of these numbers is 1+4+9+36=50.

	Let sigma2(n) represent the sum of the squares of the divisors of n. Thus sigma2(6)=50.

	Let SIGMA2 represent the summatory function of sigma2, that is SIGMA2(n)=sigma2(i) for i=1 to n.
	The first 6 values of SIGMA2 are: 1,6,16,37,63 and 113.
	Find SIGMA2(10^15) modulo 109.
	"""
	import sys, time

	sys.path.insert(0, "../general_math")
	number = int(sys.argv[1])
	start = time.time()
	answer = SIGMA2(number)
	end = time.time()
	
	print answer, end - start