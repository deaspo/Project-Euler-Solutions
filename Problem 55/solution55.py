#! /usr/bin/env python

def isPalindrome(s):
   result = True
   size = len(s)
   j = size - 1
   i = 0
   while i <= j:
      if s[i] != s[j]:
         result = False      
      j -= 1
      i += 1   
   return result;

cnt = 0
for i in range(1, 10000):
   n = i
   for j in range(50):
      m = n + int(str(n)[::-1])
      if isPalindrome(str(m)):
         cnt += 1
         break
      else:
         n += int(str(n)[::-1])
print 9999 - cnt
