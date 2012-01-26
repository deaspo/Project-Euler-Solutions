#! /usr/bin/env python 
from fraction import *
from math import *

if __name__ == "__main__":
   sum = 0
   n = 200
   a = (1, 2, 5, 10, 20, 50, 100, 200)
   c1 = 0
   c1Max = n / a[0]
   while (c1 <= c1Max):
      c2 = 0
      c2Max = (n - c1 * a[0]) / a[1]
      while (c2 <= c2Max):
         c3 = 0
         c3Max = (n - c1 * a[0] - c2 * a[1]) / a[2]
         while (c3 <= c3Max):
            c4 = 0
            c4Max = (n - c1 * a[0] - c2 * a[1] - c3 * a[2]) / a[3]
            while (c4 <= c4Max):
               c5 = 0
               c5Max = (n - c1 * a[0] - c2 * a[1] - c3 * a[2] - c4 * a[3]) / a[4]
               while (c5 <= c5Max):
                  c6 = 0
                  c6Max = (n - c1 * a[0] - c2 * a[1] - c3 * a[2] - c4 * a[3] - c5 * a[4]) / a[5]
                  while (c6 <= c6Max):
                     c7 = 0
                     c7Max = (n - c1 * a[0] - c2 * a[1] - c3 * a[2] - c4 * a[3] - c5 * a[4] - c6 * a[5]) / a[6]
                     while (c7 <= c7Max):
                        c8 = 0
                        c8Max = (n - c1 * a[0] - c2 * a[1] - c3 * a[2] - c4 * a[3] - c5 * a[4] - c6 * a[5] - c7 * a[6]) / a[7]
                        while (c8 <= c8Max):
                           lhs = 0
                           c = (c1, c2, c3, c4, c5, c6, c7, c8)
                           for i in range(len(a)):
                              lhs += c[i] * a[i]
                           if lhs == n:
                              sum += 1
                           c8 += 1
                        c7 += 1
                     c6 += 1
                  c5 += 1
               c4 += 1
            c3 += 1
         c2 += 1
      c1 += 1
   print 'Answer:', sum