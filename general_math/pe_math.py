FIRST_100_PRIME_NUMBERS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                           47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
                           107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
                           167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
                           229, 233, 239, 241, 251, 257, 263 ,269, 271, 277, 281,
                           283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353,
                           359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421,
                           431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
                           491, 499, 503, 509, 521, 523, 541]

def is_prime(number):
    """
    Checkes whether number is a prime.
    @param number: The number to check for prime status.
    @type number: int
    return: True if number is prime.
    returntype: boolean
    """
    is_prime = (number > 1) and ((number == 2) or (number == 3))
    is_prime =  is_prime or ((number % 2 != 0) and (number % 3 != 0))
               
    if is_prime and (number > 3):
        divisor = 6
        while is_prime and ((divisor - 1)**2 <= number):
            is_prime = (number % (divisor - 1) != 0) and \
                       (number % (divisor + 1) != 0)
            divisor += 6
    return is_prime

def generate_list_of_primes(upper_limit):
    """
    Generates a list of prime numbers in the interval [2, upper_limit]
    @param upper_limit: A positive integer
    @type upper_limit: int
    @return: List of prime numbers
    @returntype: [int]
    """
    is_prime = [True] * (upper_limit + 1)
    is_prime[0] = is_prime[1] = False
    
    p = 2
    while p * p <= upper_limit:
        j = p * p
        while j <= upper_limit:
            is_prime[j] = False
            j += p
        
        p += 1
        while not is_prime[p]:
            p += 1
    
    return [number for number in xrange(upper_limit) if is_prime[number]]

def get_divisors(number):
    """
    Given a number returns all divisors of it.
    @param number: Number to get divisors of.
    @type: int
    @return: List of divisors
    @returntype: [int]
    """
    return set(reduce(list.__add__, ([i, number/i] for i in xrange(1, int(number**0.5) + 1) if number % i == 0)))

def get_divisors2(number):
    def find_factors(prime_divisors, multiplicity, current_divisor, current_result):
        if current_divisor == len(prime_divisors):
            return current_result

        for (i in xrange(multiplicity[currentDivisor])):
            find_factors(prime_divisors, multiplicity, current_divisor + 1, current_result)
            current_result *= primeDivisors[currentDivisor]


def get_prime_factors(number):
    """
    Given a number returns all prime divisors of it such that the product of the divisors are number.
    @param number: Number to get prime divisors of.
    @type: int
    @return: List of prime divisors
    @returntype: [int]
    """
    limit = int(number**0.5) + 1
    primes = generate_list_of_primes(limit)
    factors = []
    for prime in primes:
        while number % prime == 0:
            number /= prime;
            factors.append(prime)

    return factors

if __name__ == "__main__":
    print 'Running tests.'
    
    # Test 1
    failed = False
    for number in FIRST_100_PRIME_NUMBERS:
        if not is_prime(number):
            print 'is_prime failed to identify ' + str(number) + ' as a prime number.'
            failed = True
            break
    
    if not failed:
        print '1. is_prime successfully identified the first 100 prime numbers!'
    
    # Test 2
    failed = False
    list_of_primes = generate_list_of_primes(FIRST_100_PRIME_NUMBERS[-1] + 1)
    if list_of_primes != FIRST_100_PRIME_NUMBERS:
        print 'generate_primes failed to generate a list equal to ' + str(FIRST_100_PRIME_NUMBERS)
        print 'instead it generated ' + str(list_of_primes)
        failed = True
    
    if not failed:
        print '2. generate_primes successfully generated a list equal to the first 100 primes.'
    
    # Test 3
    failed = False
    list_of_primes = generate_list_of_primes(100000)
    for prime in list_of_primes:
        if not is_prime(prime):
            print 'is_prime failed to identify ' + str(number) + ' as a prime number.'
            failed = True
            break
    
    if not failed:
        print '3. is_prime successfully identified all primes up to ' + str(list_of_primes[-1])
        
    # Test 4
    failed = False
    list_of_non_primes = [67311, 11673, 713]
    for non_prime in list_of_non_primes:
        if is_prime(non_prime):
            failed = True
            print 'is_prime failed to detect ' + str(non_prime) + ' as a non prime.'

    if not failed:
        print "4. is_prime didn't flag any of the chosen non primes as primes"

    # Test 5
    failed = False
    expected_divisors = [1, 2, 3, 6]
    for i in get_divisors(6):
        if not i in expected_divisors:
            failed = True
            print 'Failed to find all divisors of 6'

    if not failed:
        print '5. get_divisors found all divisors of 6'

    # Test 6
    failed = False
    expected_divisors = [1, 3, 5, 15]
    for i in get_divisors(15):
        if not i in expected_divisors:
            failed = True
            print 'Failed to find all divisors of 15'

    if not failed:
        print '6. get_divisors found all divisors of 15'

    # Test 7
    failed = False
    expected_factors = [5, 7, 13, 29]
    product = 1
    number = 13195
    for x in get_prime_factors(number):
        product *= x

    if product != number:
        print "Failed to get prime factors of " + str(number)
    else:
        print "7. Found all factors of " + str(number)

    # Test 8
    failed = False
    expected_factors = [5, 7, 13, 29]
    product = 1
    number = 4000000000
    for x in get_prime_factors(number):
        product *= x

    if product != number:
        print "Failed to get prime factors of " + str(number)
    else:
        print "8. Found all factors of " + str(number)
