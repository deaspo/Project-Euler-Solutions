#include <iostream>
#include <vector>

using namespace std;
bool isPrime(int num);
vector<unsigned> generatePrimes(unsigned limit);
unsigned *primes;

int main(void) {
   vector<unsigned> p = generatePrimes(1000);
   int a, b, best_a, best_b;
   unsigned n, cnt, best_cnt = 0;
   primes = new unsigned[p.size()];
   for (n = 0; n < p.size(); n++)
      primes[n] = p[n];

   for (a = -999; a < 1000; a += 2) {
      for (b = 0; primes[b] < 1000; b++) {
         cnt = 0;
         for(n = 0; isPrime(n*n + a*n + primes[b]); n++)
            cnt++;
         if (cnt > best_cnt) {
            best_cnt = cnt;
            best_a = a;
            best_b = primes[b];
         }
      }
   }
   delete primes;
   cout << best_a*best_b << endl;
   return 0;
}

bool isPrime(int num) {
   if (num < 2)
      return false;
   else {
      for (int i = 0; primes[i]*primes[i] <= num; i++)
         if (num % primes[i] == 0)
            return false;
   }
   return true;
}

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
