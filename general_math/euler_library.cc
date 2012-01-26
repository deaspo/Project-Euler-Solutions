#include "euler_library.h"

/* Function generates prime numbers up to num using Sieve's algorithm */
vector<unsigned> generatePrimes(unsigned limit) {
   int i, j, p;
   bool *numbers = new bool[limit + 1];
   vector<unsigned> primes;
   numbers[0] = numbers[1] = false;
   for (i = 2; i <= limit; i++)
      numbers[i] = true;
   p = 2;
   while (p*p <= limit) {
      j = p*p;
      while (j <= limit) {
         numbers[j] = false;
         j += p;
      }
      do p++; while (!numbers[p]);
   }
   for (i = 0; i < limit; i++)
      if (numbers[i])
         primes.push_back(i);
   delete numbers;
   return primes;
}

/* Function returns true if num is a prime number */
bool isPrime(unsigned num) {
   bool prime = true;
   if (num == 2 or num == 3);
   else if (num % 2 == 0 or num % 3 == 0)
      prime = false;
   else {
      for (int k = 6; (k - 1)*(k - 1) <= num and prime; k += 6)
         if (num % (k - 1) == 0 or num % (k + 1) == 0)
            prime = false;
   }
   return prime;
}

/* Function returns the sum of coprimes (< n) to n */
unsigned int phi(unsigned n) {
   float fac;
   if (isPrime(n))
      fac = (float)n - 1.0;
   else {
      unsigned p = 3, limit = n;
      fac = (n % 2 == 0) ? (float)n*0.5 : (float)n;
      while (p <= limit) {
         if (n % p == 0) {
            fac *= (1.0 - 1.0/(float)p);
            limit /= p;
         }
         p += 2;
         while (!isPrime(p)) p += 2;
      }
   }
   return (unsigned int)fac;
}

/* Converts an int n to vector num, 345 -> [3,4,5]*/
void toVector(vector<int>& num, int n) {
   num.clear();
   while (n > 0) {
      num.push_back(n % 10);
      n /= 10;
   }
}

/* Converts a vector num to an int, [3,4,5] -> 345 */
unsigned toInt(const vector<int>& num) {
   unsigned n = 0, p = 1;
   for (int i = 0; i < num.size(); i++) {
      n += num[i]*p;
      p *= 10;
   }
   return n;
}

/* Checks wether a number is abundant */
bool isAbundant(int num) {
   int i, sum = 0, limit = (int)sqrt(num);
   for (i = 1; i <= limit; i++)
      if (num % i == 0)
         sum += (i == num/i) ? i : i + num/i;
   return (sum > 2*num) ? true : false;
}

/* Returns the sum of all divisors to num */
int sumOfDivisors(int num) {
   int i, sum = 1, limit = (int)sqrt(num);
   for (i = 2; i <= limit; i++)
      if (num % i == 0)
         sum += (i == num/i) ? i : i + num/i;
   return sum;
}

/* Returns the greates common divisor of a and b */
int gcd(int a, int b) {
  int t;
  while (b != 0) {
    t = b;
    b = a % b;
    a = t;
  }
  return a;
}

/* Returns true if m and n are permutations of each others */
bool isPermutation(unsigned m, unsigned n) {
   toVector(v1, m);
   toVector(v2, n);
   bool found;
   unsigned size = v1.size(), cnt = 0;
   if (size == v2.size()) {
      for (int i = 0; i < size; i++) {
         found = false;
         for (int j = 0; j < size and !found; j++) {
            if (v1[i] == v2[j]) {
               cnt++;
               v2[j] = -1; // Make sure it isn't selected again
               found = true;
            }
         }
      }
   }
   return (cnt == size) ? true : false;
}

unsigned fac(unsigned limit) {
   if (limit == 0)
      return 1;
   else {
      int n = 1, i;
      for (i = 1; i <= limit; i++)
         n *= i;
   }
   return n;
}

bool isPalindrome(const string& s) {
   bool result = true;
   int size = s.size();
   int j = size - 1;
   
   for (int i = 0; i <= j; i++) {
      if (s[i] != s[j])
         result = false;      
      j--;
   }
   
   return result;
}
