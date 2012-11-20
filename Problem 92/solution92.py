def main():
	limit = 10000000
	answer = 0
	for starting_number in range(1, limit):
		number = starting_number
		number_series = [number]
		while number not in (1, 89):
			number = get_next_number(number)
		if number == 89:
			answer += 1
	return answer

def get_next_number(number):
	return sum([int(digit)*int(digit) for digit in str(number)])

if __name__ == "__main__":
    from time import time
    start = time()
    answer = main()
    end = time()
    print answer, end - start