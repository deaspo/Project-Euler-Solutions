#! /usr/bin/env python 

from copy import *

def generatePrimes(upperLimit):
   # Initiate markup list
   isPrime = [False, False]
   for i in range(2, upperLimit + 1):
      isPrime.append(True);

   # Mark numbers which cannot be primes
   p = 2
   while p * p <= upperLimit:
      j = p * p
      while j <= upperLimit:
         isPrime[j] = False
         j += p
      p += 1
      while not isPrime[p]:
         p += 1

   # Add all numbers which must be primes to list
   primes = []
   for i in range(0, upperLimit):
      if isPrime[i]:
         primes.append(i)
   return primes


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


def str2list(string):
   # '123' -> [1, 2, 3]
   number = []
   for digit in string:
      number.append(int(digit))
   return number


def sequence2number(sequence):
   # [1, 2, 3] -> '123'
   tmp = ''
   for digit in sequence:
      tmp += str(digit)
   return int(tmp)


def getPrimeFamily(number, indices):
   # Identifies a prime family by replacing digits at positions indicated by indices.
   tmpFamily = []
   for k in range(10):
      tmpSeq = copy(number)
      for i in range(len(indices)):
         tmpSeq[indices[i]] = k
      tmp = sequence2number(tmpSeq)
      if isPrime(tmp) and (not tmp in tmpFamily) and (len(tmpSeq) == len(str(tmp))):
         tmpFamily.append(tmp)
   return tmpFamily


def getLongestPrimeFamily(number):
   family = []
   number = str2list(str(number))
   length = len(number)

   if length == 6: # number in [100000, 999999]
      # Replace up to five digits
      for i in range(length):
         j = 0
         while j <= i:
            k = 0
            while k <= j:
               l = 0
               while l <= k:
                  m = 0
                  while m <= l:
                     tmpFamily = getPrimeFamily(number, [i, j, k, l, m])
                     if len(tmpFamily) > len(family):
                        family = copy(tmpFamily)
                     m += 1
                  l += 1
               k += 1
            j += 1
   elif length == 5: # number in [10000, 99999]
      # Replace up to four digits
      for i in range(length):
         j = 0
         while j <= i:
            k = 0
            while k <= j:
               l = 0
               while l <= k:
                  tmpFamily = getPrimeFamily(number, [i, j, k, l])
                  if len(tmpFamily) > len(family):
                     family = copy(tmpFamily)
                  l += 1
               k += 1
            j += 1
   elif length == 4: # number in [1000, 9999]
      # Replace up to three digits
      for i in range(length):
         j = 0
         while j <= i:
            k = 0
            while k <= j:
               tmpFamily = getPrimeFamily(number, [i, j, k])
               if len(tmpFamily) > len(family):
                  family = copy(tmpFamily)
               k += 1
            j += 1
   elif length == 3: # number in [100, 999]
      # Replace up to two digits
      for i in range(length):
         j = 0
         while j <= i:
            tmpFamily = getPrimeFamily(number, [i, j])
            if len(tmpFamily) > len(family):
               family = copy(tmpFamily)
            j += 1
   elif length == 2: # number in [10, 99]
      # Replace one digit
      for i in range(length):
         tmpFamily = getPrimeFamily(number, [i])
         if len(tmpFamily) > len(family):
            family = copy(tmpFamily)
   elif length == 1:
      family = getPrimeFamily(number, [0])
   else:
      raise ValueError, sequence2str(number) + ' is too large for getLongestPrimeFamily'
   
   return family

   
if __name__ == "__main__":
   found = False
   upperLimit = 1000000
   primes = generatePrimes(upperLimit)
   i = 0
   while (not found) and (i < len(primes)):
      family = getLongestPrimeFamily(primes[i])
      if len(family) == 8:
         found = True
      i += 1
      
   print 'Answer:', family[0]
   