def fac(n):
   if n != 0:
      tmp, i = 1, 1
      while (i <= n):
         tmp *= i
         i += 1
      return tmp
   else:
      return 1;

def nCr(n, r):
   return fac(n)/(fac(r)*fac(n - r))

def run():
   cnt = 0
   for n in range(1, 101):
      for r in range(1, n + 1):
         if (nCr(n, r) > 1000000):
            cnt += 1
   print 'There are', cnt, 'values of n that exceeds one million'
