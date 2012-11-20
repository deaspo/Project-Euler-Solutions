def main():
	"""
	A common security method used for online banking is to ask the user for three random 
	characters from a passcode. For example, if the passcode was 531278, they may ask for 
	the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

	The text file, keylog.txt, contains fifty successful login attempts.

	Given that the three characters are always asked for in order, analyse the file so 
	as to determine the shortest possible secret passcode of unknown length.
	"""
	import operator, time

	start = time.time()
	numbers = getNumbersFromFile()
	positions = getPositions(numbers)
	averagePositions = getAveragePositions(positions)
	answer = "".join([k for k,v in sorted(averagePositions.iteritems(), key=operator.itemgetter(1)) if v > 0])
	end = time.time()

	print answer, end - start

def getAveragePositions(positions):
	averagePositions = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
	for key in positions:
		if len(positions[key]) > 0:
			averagePositions[key] += sum(positions[key]) / float(len(positions[key]))

	return averagePositions

def getPositions(numbers):
	positions = {'0':[], '1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[], '9':[]}

	for number in numbers:
		positions[number[0]].append(1)
		positions[number[1]].append(2) 
		positions[number[2]].append(3)

	return positions

def getNumbersFromFile():
	numbers = []
	file_stream = open("keylog.txt", "r")
	[numbers.append(line) for line in file_stream]
	file_stream.close()

	return numbers

if __name__ == "__main__":
	main()