#include <iostream>
#include <vector>
#define LIMIT 10000000
using namespace std;

vector<int> v1, v2;
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

void toArray(vector<int>& num, int n) {
   num.clear();
   while (n > 0) {
      num.push_back(n % 10);
      n /= 10;
   }
}

bool isPermutation(unsigned m, unsigned phi_n) {
   toArray(v1, m);
   toArray(v2, phi_n);
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

unsigned int phi(unsigned n) {
   double fac = (double)n;
   unsigned p = 3, i = 0;
   while (p <= n) {
      if (n % p == 0) {
         fac *= (1.0 - 1.0/(double)p);
         n /= p;
      }
      p = primes[i++];
   }
   return (p != n) ? (unsigned int)fac : n - 1;
}

int main() {
   unsigned i, j, n, best_i;
   float frac = 0.0, min_frac = 10.0;

   vector<unsigned> p = generatePrimes(LIMIT);
   primes = new unsigned[p.size()];
   for (i = 0; i < p.size(); i++) 
      primes[i] = p[i];

   for (i = 3; i < LIMIT; i += 2) {
      n = phi(i);
      frac = (double)i/(double)n;
      if (frac < min_frac) {
         if (isPermutation(i, n)) {
            min_frac = frac;
            best_i = i;
            cout << "i = " << i << ", phi(i) = " << n << ", i/phi(i) = " << min_frac << endl;
         }
      }
   }
   cout << best_i << endl;
   delete primes;
   exit(EXIT_SUCCESS);
}
