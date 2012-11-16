def get_divisors(number):
    """
    Given a number returns all divisors of it.
    @param number: Number to get divisors of.
    @type: int
    @return: List of divisors
    @returntype: [int]
    """
    return set(reduce(list.__add__, ([i, number/i] for i in xrange(1, int(number**0.5) + 1) if number % i == 0)))

def sigma2(number):
	"""
	Returns the sum of all squared divisors of number
	"""
	return sum([x*x for x in get_divisors(number)]) 

def SIGMA2(number):
	return sum(sigma2(i) for i in xrange(1, number + 1))

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

	number = int(sys.argv[1])
	start = time.time()
	answer = SIGMA2(number)
	end = time.time()

	print "SIGMA2(" + str(number) + ") = " + str(answer)
	print "time = " + str(end - start) + " sec."
	