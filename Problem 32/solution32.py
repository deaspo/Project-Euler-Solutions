#! /usr/bin/env python

def toList(n):
   num = []
   while (n > 0):
      num.append(n % 10)
      n /= 10
   return num

def isPermutation(m, n):
   v1 = toList(m)
   v2 = toList(n)
   size, cnt = len(v1), 0
   if size == len(v2):
      for i in range(0, size):
         found = False
         for j in range(0, size):
            if v1[i] == v2[j]:
               cnt += 1
               v2[j] = -1
               found = True
            if found == True:
               break
   if cnt == size:
      return True
   else:
      return False

sum = 0
prod = []
for multiplicand in range(1, 2000):
   multiplier, n = 0, '0'
   while len(n) <= 9:
      multiplier += 1
      m = multiplicand*multiplier
      n = str(multiplicand) + str(multiplier) + str(m)
      if len(n) == 9:
         if isPermutation(123456789, int(n)):
            if m not in prod:
               prod.append(m)

for i in range(0, len(prod)):
   sum += prod[i]
print sum

