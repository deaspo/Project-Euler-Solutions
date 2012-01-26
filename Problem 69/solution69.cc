#include <iostream>
#include <cmath>
#include <vector>
#define LIMIT 1000000
using namespace std;

unsigned *primes;

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

unsigned int phi(unsigned n) {
   double fac = (double)n;
   unsigned p = 2, i = 0;
   while (p*p <= n) {
      if (n % p == 0)
         fac *= (1.0 - 1.0/(double)p);
      p = primes[++i];
   }
   return (unsigned int)fac;
}

int main() {
   unsigned n, best_n;
   double frac = 0.0, best_frac = -1.0;
   
   vector<unsigned> p = generatePrimes(LIMIT);
   primes = new unsigned[p.size()];
   for (n = 0; n < p.size(); n++) 
      primes[n] = p[n];

   for (n = 2; n <= LIMIT; n += 2) {
      frac = (double)n / (double)phi(n);
      if (frac > best_frac) {
         best_frac = frac;
         best_n = n;
      }
   }
   cout << best_n << endl;
   delete primes;
   exit(EXIT_SUCCESS);
}
