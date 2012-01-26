#! /usr/bin/env python 
from fraction import *

def isPrime(num):
      # Decides wheter a number is prime or not
      prime = True
      if (num != 2) and (num != 3):
         if num < 2:
            prime = False
         elif (num % 2 == 0) or (num % 3 == 0):
            prime = False
         elif num > 3:
            k = 6
            while ((k - 1) * (k - 1) <= num) and prime:
               if (num % (k - 1) == 0) or (num % (k + 1) == 0):
                  prime = False;
               k = k + 6
      return prime;

if __name__ == "__main__":
   limit = 11
   sum = 0
   answer = 0
   number = 11
   while sum < limit:
      if isPrime(number):
         remainsPrime = True
         
         # Remove digits from left one at a time
         tmp = str(number)
         while (len(str(tmp)) > 1) and remainsPrime:
            tmp = tmp[1:]
            if not isPrime(int(tmp)):
               remainsPrime = False
            
         # Remove digits from right one at a time
         tmp = str(number)
         while (len(str(tmp)) > 1) and remainsPrime:
            tmp = tmp[:len(tmp) - 1]
            if not isPrime(int(tmp)):
               remainsPrime = False
         
         if remainsPrime:
            sum += 1
            answer += number
      number += 2
   print 'Answer:', answer