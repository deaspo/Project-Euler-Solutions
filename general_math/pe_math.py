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
        print 'is_prime successfully identified the first 100 prime numbers!'
    
    # Test 2
    failed = False
    list_of_primes = generate_list_of_primes(FIRST_100_PRIME_NUMBERS[-1] + 1)
    if list_of_primes != FIRST_100_PRIME_NUMBERS:
        print 'generate_primes failed to generate a list equal to ' + str(FIRST_100_PRIME_NUMBERS)
        print 'instead it generated ' + str(list_of_primes)
        failed = True
    
    if not failed:
        print 'generate_primes successfully generated a list equal to the first 100 primes.'
    
    # Test 3
    failed = False
    list_of_primes = generate_list_of_primes(100000)
    for prime in list_of_primes:
        if not is_prime(prime):
            print 'is_prime failed to identify ' + str(number) + ' as a prime number.'
            failed = True
            break
    
    if not failed:
        print 'is_prime successfully identified all primes up to ' + str(list_of_primes[-1])
        
    # Test 4
    list_of_non_primes = [67311, 11673, 713]
    for non_prime in list_of_non_primes:
        if is_prime(non_prime):
            print 'is_prime failed to detect ' + str(non_prime) + ' as a non prime.'
