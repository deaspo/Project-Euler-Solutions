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

max = 0
for i in range(1, 10000):
   j, num = 1, ''
   while len(num) < 9:
      num += str(i*j)
      j += 1
      if len(num) == 9:
         if isPermutation(123456789, int(num)):
            if int(num) > max:
               max = int(num)
print max
