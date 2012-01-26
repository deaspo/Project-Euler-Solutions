import math

def calcAmicableSum(limit):
   sum = 0
   for i in range(1, limit):
      for j in range(1, limit):
         if (i != j):
            if (d(i) == j) and (d(j) == i):
               sum += i
               print i, "and", j, "-> sum =", sum
   print "Total sum is", sum

def d(num):
   sum, limit = 1, int(math.sqrt(num))
   for i in range(2, limit):
      if (num % i == 0):
         sum += i + num/i
   return sum

