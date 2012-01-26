def slow_solution():
    from pe_math import is_prime, generate_list_of_primes
    MAX_NUMBER = 10000
    list_of_primes = generate_list_of_primes(MAX_NUMBER)
    number_of_primes = len(list_of_primes)
    primes = [0, 0, 0, 0 ,0]
    for i1 in xrange(number_of_primes - 4):
        prime_1 = list_of_primes[i1]
        for i2 in xrange(i1 + 1, number_of_primes - 3):
            prime_2 = list_of_primes[i2]
            if all_concatenations_are_prime_numbers(prime_1, prime_2):
                for i3 in xrange(i2 + 1, number_of_primes - 2):
                    prime_3 = list_of_primes[i3]
                    if all_concatenations_are_prime_numbers(prime_1, prime_2, prime_3):
                        for i4 in xrange(i3 + 1, number_of_primes - 1):
                            prime_4 = list_of_primes[i4]
                            if all_concatenations_are_prime_numbers(prime_1, prime_2, prime_3, prime_4):
                                for i5 in xrange(i4 + 1, number_of_primes):
                                    prime_5 = list_of_primes[i5]
                                    if all_concatenations_are_prime_numbers(prime_1, prime_2, prime_3, prime_4, prime_5):
                                        return [prime_1, prime_2, prime_3, prime_4, prime_5]
    return primes

def all_concatenations_are_prime_numbers(prime_1, \
                                         prime_2, \
                                         prime_3=None, \
                                         prime_4=None, \
                                         prime_5=None):
    """
    Tries all concatenations of four prime numbers.
    @param prime_1: An integer
    @type prime_1: int
    @param prime_2: An integer
    @type prime_2: int
    @param prime_3: An integer
    @type prime_3: int
    @param prime_4: An integer
    @type prime_4: int
    @param prime_5: An integer
    @type prime_5: int
    @return: True if all concatenations are prime numbers
    @returntype: boolean
    """
    from pe_math import is_prime
    are_prime = is_prime(concatenate(prime_1, prime_2)) and \
                is_prime(concatenate(prime_2, prime_1))
    if are_prime and prime_3:
        are_prime = is_prime(concatenate(prime_1, prime_3)) and \
                    is_prime(concatenate(prime_3, prime_1)) and \
                    is_prime(concatenate(prime_2, prime_3)) and \
                    is_prime(concatenate(prime_3, prime_2))
    if are_prime and prime_4:
        are_prime = is_prime(concatenate(prime_1, prime_4)) and \
                    is_prime(concatenate(prime_4, prime_1)) and \
                    is_prime(concatenate(prime_2, prime_4)) and \
                    is_prime(concatenate(prime_4, prime_2)) and \
                    is_prime(concatenate(prime_3, prime_4)) and \
                    is_prime(concatenate(prime_4, prime_3))
    if are_prime and prime_5:
        are_prime = is_prime(concatenate(prime_1, prime_5)) and \
                    is_prime(concatenate(prime_5, prime_1)) and \
                    is_prime(concatenate(prime_2, prime_5)) and \
                    is_prime(concatenate(prime_5, prime_2)) and \
                    is_prime(concatenate(prime_3, prime_5)) and \
                    is_prime(concatenate(prime_5, prime_3)) and \
                    is_prime(concatenate(prime_4, prime_5)) and \
                    is_prime(concatenate(prime_5, prime_4))
    return are_prime

def concatenate(a, b):
    """
    Concatenates two numbers
    @param a: An integer
    @type a: int
    @param b: An integer
    @type b: int
    @return: The concatenation of the numbers.
    @returntype: int
    """
    return int(str(a) + str(b))

if __name__ == "__main__":
    from time import time
    start = time()
    primes = slow_solution()
    end = time()
    print 'Answer is: ' + str(primes[0] + primes[1] + primes[2] + primes[3] + primes[4]) + ' and it took ' + str(end - start) + 's.'
    print 'Primes are: ' + str(primes)
