#include <iostream>
#include <vector>

using namespace std;
vector<unsigned> generatePrimes(unsigned limit);

int main(void) {
   vector<unsigned> p = generatePrimes(1000000);
   unsigned primes[p.size()], i, j, cnt, max_cnt = 0, max_sum = 0, sum;

   for (i = 0; i < p.size(); i++)
      primes[i] = p[i];

   for (i = 0; i < p.size(); i++) {
      sum = cnt = 0;
      for (j = 0; sum < primes[i]; j++) {
         sum += primes[j];
         cnt++;
      }
      if (sum > primes[i]) {
         for (j = 0; sum > primes[i]; j++) {
            sum -= primes[j];
            cnt--;
         }
      }
      if (sum == primes[i]) {
         if (cnt > max_cnt) {
            max_cnt = cnt;
            max_sum = sum;
         }
      }
   }
   cout << max_sum << endl;
   return 0;
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
