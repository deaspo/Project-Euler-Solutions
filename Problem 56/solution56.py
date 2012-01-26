#! /usr/bin/env python

def toList(n):
   num = []
   while (n > 0):
      num.append(n % 10)
      n /= 10
   return num

max_sum, sum = 0, 0
for a in range(0, 100):
   for b in range(0, 100):
      sum = 0
      n = toList(a**b)
      for i in range(0, len(n)):
         sum += n[i]
      if sum > max_sum:
         max_sum = sum
print max_sum
