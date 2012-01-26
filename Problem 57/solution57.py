#! /usr/bin/env python

from math import *
from fraction import *

if __name__ == "__main__":
   one = Fraction(1)
   two = Fraction(2)
   tmp = Fraction(0)
   sum = 0
   i = 0
   while i < 1000:
      fraction = one + one / (two + tmp)
      tmp = one / (two + tmp)
      if len(str(fraction.numerator)) > len(str(fraction.denominator)):
         sum = sum + 1
      i = i + 1
      
   print 'Answer:', sum
   