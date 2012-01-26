#! /usr/bin/env python
import sys

if __name__ == "__main__":
   sum = 0
   for i in range(1, int(sys.argv[1]) + 1):
      num = i
      for j in range(1, i):
         num *= i
      sum += num
   print sum
  

