#! /usr/bin/env python
from math import *

class Fraction:
   # Class for describing fractions
   def __init__(self, numerator = 0, denominator = 1):
      if (type(numerator) == type(int(1))) or (type(numerator) == type(long(1))):
         self.numerator = numerator
         self.denominator = denominator
         self.__reduce()
      elif type(numerator) == type(float(1)):
         self.__toFraction(numerator)
      else:
         raise ValueError, "Invalid parameter to Fraction class!"


   def __add__(self, other):
      # a/b + c/d = (ad + cb)/bd
      numerator = self.numerator * other.denominator + other.numerator * self.denominator
      denominator = self.denominator * other.denominator
      return Fraction(numerator, denominator)


   def __sub__(self, other):
      # a/b - c/d = (ad - cb)/bd
      numerator = self.numerator * other.denominator - other.numerator * self.denominator
      denominator = self.denominator * other.denominator
      return Fraction(numerator, denominator)


   def __mul__(self, other):
      # (a/b)*(c/d) = (ac)/(bd)
      numerator = self.numerator * other.numerator
      denominator = self.denominator * other.denominator
      return Fraction(numerator, denominator)


   def __div__(self, other):
      # (a/b) / (c/d) = (ad/bc)
      numerator = self.numerator * other.denominator
      denominator = self.denominator * other.numerator
      return Fraction(numerator, denominator)


   def __str__(self):
      return str(self.numerator) + "/" + str(self.denominator)


   def __reduce(self):
      # Reduces the fraction as far as possible. E.g. 10/24 becomes 5/12
      a = self.numerator
      b = self.denominator
      divisor = self.__gcd(a, b)
      self.numerator = self.numerator / divisor
      self.denominator = self.denominator / divisor


   def __gcd(self, a, b):
      # Finds the greatest common divisor of a and b
      while b != 0:
         tmp = b
         b = a % b
         a = tmp
      return a


   def __isPrime(self, num):
      # Decides wheter a number is prime or not
      prime = True
      if (num % 2 == 0) or (num % 3 == 0):
         prime = False
      elif num > 3:
         k = 6
         while ((k - 1) * (k - 1) <= num) and prime:
            if (num % (k - 1) == 0) or (num % (k + 1) == 0):
               prime = False;
            k = k + 6
      elif num <= 1:
         prime = False
      return prime;


   def __toFraction(self, number):
      # Turns a decimal number into a fraction.
      # E.g.) 3.245 becomes 649/200 using continued fractions

      # First find the continued fractions of 'number'
      maxIter = 25   # In case number is an irrational number and won't converge
      eps = 1.0e-9
      rest = number
      integerParts = [int(rest)]
      i = 0
      while (i < maxIter - 1) and (abs(rest - integerParts[i]) > eps):
         rest = 1.0 / (rest - integerParts[i])
         if abs(rest - round(rest)) < eps:
            rest = round(rest)   # This will prevent round off errors
         integerParts.append(int(rest))
         i = i + 1

      # Print warning if approximation has been done
      if i == maxIter - 1:
         print 'Warning!', number, 'has been approximated.'
     
      # Now create the fraction using the integerParts
      i = len(integerParts) - 1
      tmp = Fraction(1, integerParts[i])
      one = Fraction(1)
      while i > 0:
         i = i - 1
         tmp = one / (Fraction(integerParts[i]) + tmp)
      tmp = one / tmp
      self.numerator = tmp.numerator
      self.denominator = tmp.denominator


   def toDecimal(self, precision = 0):
      # Returns the decimal notation of the fraction
      if precision == 0:
         return self.numerator / float(self.denominator)
      else:
         print 'Not implemented yet.'

