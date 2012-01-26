#! /usr/bin/env python 

def next_permutation(seq, pred=cmp):
    """Like C++ std::next_permutation() but implemented as
    generator. Yields copies of seq."""

    def reverse(seq, start, end):
        # seq = seq[:start] + reversed(seq[start:end]) + \
        #       seq[end:]
        end -= 1
        if end <= start:
            return
        while True:
            seq[start], seq[end] = seq[end], seq[start]
            if start == end or start+1 == end:
                return
            start += 1
            end -= 1
    
    if not seq:
        raise StopIteration

    try:
        seq[0]
    except TypeError:
        raise TypeError("seq must allow random access.")

    first = 0
    last = len(seq)
    seq = seq[:]

    # Yield input sequence as the STL version is often
    # used inside do {} while.
    yield seq
    
    if last == 1:
        raise StopIteration

    while True:
        next = last - 1

        while True:
            # Step 1.
            next1 = next
            next -= 1
            
            if pred(seq[next], seq[next1]) < 0:
                # Step 2.
                mid = last - 1
                while not (pred(seq[next], seq[mid]) < 0):
                    mid -= 1
                seq[next], seq[mid] = seq[mid], seq[next]
                
                # Step 3.
                reverse(seq, next1, last)

                # Change to yield references to get rid of
                # (at worst) |seq|! copy operations.
                yield seq[:]
                break
            if next == first:
                raise StopIteration
    raise StopIteration

def subStringDivisible(number, divisors):
   number = str(number)
   for i in range(len(number) - 3):
      subString = number[i + 1:i + 4]
      if int(subString) % divisors[i] != 0:
         return False
   return True

def fac(n):
   factorial = 1
   for j in range(2, n + 1):
      factorial *= j
   return factorial
   
if __name__ == "__main__":
   numbersWithDivisibilityProperty = []
   divisors = (2, 3, 5, 7, 11, 13, 17)
   for number in next_permutation([1,2,3,4,5,6,7,8,9,0]):
      numberStr = ''
      for digit in number:
         numberStr += str(digit)
         
      if subStringDivisible(numberStr, divisors):
         numbersWithDivisibilityProperty.append(numberStr)

   sum = 0
   for number in numbersWithDivisibilityProperty:
      sum += int(number)

   print 'Answer:', sum