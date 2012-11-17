def main():
    MAX_NUMBER = 10000
    triangle_numbers = get_list_of_numbers(MAX_NUMBER, triangle) # 96 numbers
    square_numbers = get_list_of_numbers(MAX_NUMBER, square) # 68 numbers
    pentagonal_numbers = get_list_of_numbers(MAX_NUMBER, pentagonal) # 56 numbers
    hexagonal_numbers = get_list_of_numbers(MAX_NUMBER, hexagonal) # 48 numbers
    heptagonal_numbers = get_list_of_numbers(MAX_NUMBER, heptagonal) # 43 numbers
    octagonal_numbers = get_list_of_numbers(MAX_NUMBER, octagonal) # 40 numbers
    for p3 in triangle_numbers:
        for p4 in pentagonal_numbers:
            for p5 in square_numbers:
                if is_cyclic([p3, p4, p5]):
                    return [p3, p4, p5]
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

def triangle(n):
    return n * (n + 1) / 2

def square(n):
    return n * n

def pentagonal(n):
    return n * (3 * n - 1) / 2

def hexagonal(n):
    return n * (2 * n - 1)

def heptagonal(n):
    return n * (5 * n - 3) / 2

def octagonal(n):
    return n * (3 * n - 2)

if __name__ == "__main__":
    from time import time
    start = time()
    numbers = main()
    end = time()
    #print 'Answer is: ' + str(numbers[0] + numbers[1] + numbers[2] + numbers[3]) + ' and it took ' + str(end - start) + 's.'
    print 'Numbers are: ' + str(numbers)
