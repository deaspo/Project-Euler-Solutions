#! /usr/bin/env python 
from fraction import *
from math import *

if __name__ == "__main__":
   # First create the continued fraction of e
   length = 100
   w = [2, 1, 2]
   k = 2
   i = 0
   while len(w) < length:
      if i % 2 == 0:
         w.append(1)
         w.append(1)
      else:
         w.append(2 * k)
         k += 1
      i += 1

   # Copy the length first numbers to e
   e = []
   for i in range(length):
      e.append(w[i])
   
   # Create a fraction for the list
   i = len(e) - 1
   a = Fraction(e[i])
   while i > 0:
      i -= 1
      tmp = Fraction(1) / a
      a = Fraction(e[i]) + tmp

   # Add all elements in numerator of a
   numerator = str(a.numerator)
   sum = 0
   for i in range(len(numerator)):
      sum += int(numerator[i])

   print 'Answer:', sum
