#! /usr/bin/env python

def isPalindrome(n):
   result = True
   j = len(n) - 1
   i = 0
   while i <= j:
      if n[i] != n[j]:
         result = False
      i += 1
      j += -1
   
   return result

def toBase(b,n,result=''):
    if n == 0:
        if result:
            return result
        else:
            return '0'
    else:
        return toBase(b,n/b,str(n%b)+result)

sum = 0
for n in range(1, 1000001):
   if isPalindrome(str(n)):
      if isPalindrome(toBase(2, n)):
         sum += n
print sum
