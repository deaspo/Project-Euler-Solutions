def main():
    MAX_NUMBER = 10000
    numbers = []
    for f in [P3, P4, P5]:
        numbers.extend(get_list_of_numbers(MAX_NUMBER, f))
    numbers = set(numbers)

    limit = len(numbers)
    for i in range(limit):
        for j in range(i, limit):
            for k in range(j, limit):
                if is_cyclic([i, j, k]) and ((isP3(i) and isP4(j) and isP5(k)) or \
                                             (isP3(i) and isP4(k) and isP5(j)) or \
                                             (isP3(j) and isP4(i) and isP5(k)) or \
                                             (isP3(j) and isP4(k) and isP5(i)) or \
                                             (isP3(k) and isP4(i) and isP5(j)) or \
                                             (isP3(k) and isP4(j) and isP5(i))):
                    return [i, j, k]

    return None


def is_cyclic(numbers):
    """
    Checks if numbers in list are cyclic
    @param numbers: List of numbers
    @type: [int]
    @return: True if numbers are cyclic
    """
    for i in range(len(numbers) - 1):
        cyclic = (str(numbers[i])[2:] == str(numbers[i + 1])[:2])
        if not cyclic:
            return False
    
    return (str(numbers[-1])[2:] == str(numbers[0])[:2])


def get_list_of_numbers(max_number, polygonal_function):
    """
    Generates a list of four digit numbers up to maximum number as a polygonal series
    defined by geometric function.
    """
    n = 1
    number = polygonal_function(n)
    numbers = []
    while number < max_number:
        if is_four_digits(number):
            numbers.append(number)
        n += 1
        number = polygonal_function(n)
    return numbers

def is_four_digits(number):
    """
    Checks that the number of digits are four.
    """
    return (number >= 1000) and (number <= 9999) 

def P3(n):
    return n * (n + 1) / 2

def isP3(n):
    return P3(int(n**0.5)) == n 

def P4(n):
    return n * n

def isP4(n):
    return P4(int(n**0.5)) == n

def P5(n):
    return n * (3 * n - 1) / 2

def isP5(n):
    return False

def P6(n):
    return n * (2 * n - 1)

def isP6(n):
    return False

def P7(n):
    return n * (5 * n - 3) / 2

def isP7(n):
    return False

def P8(n):
    return n * (3 * n - 2)

def isP8(n):
    return False

if __name__ == "__main__":
    from time import time
    start = time()
    numbers = main()
    end = time()
    #print 'Answer is: ' + str(numbers[0] + numbers[1] + numbers[2] + numbers[3])''
    print 'Numbers are: ' + str(numbers)
    print 'Time: ' + str(end - start) + 's.'
