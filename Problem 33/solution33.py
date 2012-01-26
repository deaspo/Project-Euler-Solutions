#! /usr/bin/env python 
from fraction import *

if __name__ == "__main__":
   examples = []
   for numerator in range(10, 100):
      for denominator in range(10, 100):
         if denominator > numerator:
            a = Fraction(numerator, denominator)
            num = str(numerator)
            den = str(denominator)
            if len(str(a.numerator)) == 1 and len(str(a.denominator)) == 1:
               nonTrivial = num[1] != '0' and den[1] != '0'
               case1 = (num[0] == den[0]) and (str(a.numerator) == num[1]) and (str(a.denominator) == den[1])
               case2 = (num[1] == den[0]) and (str(a.numerator) == num[0]) and (str(a.denominator) == den[1])
               case3 = (num[0] == den[1]) and (str(a.numerator) == num[1]) and (str(a.denominator) == den[0])
               case4 = (num[1] == den[1]) and (str(a.numerator) == num[0]) and (str(a.denominator) == den[0])
               unOrthodox = case1 or case2 or case3 or case4
               if nonTrivial and unOrthodox:
                  print num, '/', den, '=', a
                  examples.append(a)
               
   exampleProduct = Fraction(49, 98)   # 49/98 = 4/8 = 1/2 where 4/8 isn't detected above due to the reduces fraction a = 1/2
   for frac in examples:
      exampleProduct *= frac
   print 'Answer:', exampleProduct.denominator
