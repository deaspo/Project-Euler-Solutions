def main():
	limit = 10000000
	answer = 0
	numbers = range(1, limit)
	for starting_number in numbers:
		number = starting_number
		while number not in (1, 89):
			number = get_next_number(number, numbers)
		numbers[starting_number - 1] = number
		answer += number == 89

	return answer

def get_next_number(number, numbers):
	squared_digit_sum = 0
	while number > 0:
		squared_digit_sum += (number % 10)**2
		number /= 10

	return numbers[squared_digit_sum - 1]

if __name__ == "__main__":
    from time import time
    start = time()
    answer = main()
    end = time()
    print answer, end - start