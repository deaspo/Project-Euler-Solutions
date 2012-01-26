#include <iostream>
#include <cmath>

using namespace std;
unsigned long long getNumberOfDivisors(unsigned long long);

int main() {
   unsigned long long sum, n = 0, cnt, limit = 500;

   /* Find triangular number with more divisors than limit */
   do {
      n++;
      sum = (n + 1)*n/2;               // Get triangle number n
      cnt = getNumberOfDivisors(sum);
   }
   while (cnt <= limit);
   
   cout << "The first triangular number to have over " << limit << " divisors is " << sum << " (" << n << ")" << endl;
   return EXIT_SUCCESS;
}

inline unsigned long long getNumberOfDivisors(unsigned long long num) {
   unsigned long long i, sum = 0, limit = (unsigned long long)sqrt(num);
   for (i = 1; i <= limit; i++)
      if (num % i == 0)
         sum += (i == num/i) ? 1 : 2;
   return sum;
}

