def main():
	print T(70)
	print T(1320)

	return None

def getDimensions(size):
	"""
	Returns a list of tuples with all valid dimensions for size
	e.g. size = 70 -> [(1, 70), (2, 35), (5, 14), (7, 10)]
	"""
	return [(w, size / w) for w in set(reduce(list.__add__, ([i, size/i] for i in xrange(1, int(size**0.5) + 1) if size % i == 0))) if w <= size / w]

def T(size):
	dimensions = getDimensions(size)

if __name__ == "__main__":
    from time import time
    start = time()
    answer = main()
    end = time()
    print 'Answer: ' + str(answer)
    print 'Time: ' + str(end - start) + 's.'
