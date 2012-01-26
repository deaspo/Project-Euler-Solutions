#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(unsigned num) {
   bool prime = true;
   if (num == 2 or num == 3);
   else if (num % 2 == 0 or num % 3 == 0)
      prime = false;
   else {
      for (int k = 6; k <= sqrt(num) + 1 and prime; k += 6)
         if (num % (k - 1) == 0 or num % (k + 1) == 0)
            prime = false;
   }
   return prime;
}

int main() {
   unsigned len = 1, num = 3, p = 0, tot = 1, inc = 2, cnt = 1;
   float frac = 1.0;
   while (frac >= 0.1) {
      if (isPrime(num)) p++;
      tot++;
      frac = (float)p/(float)tot;
      num += inc;
      cnt++;
      if (cnt == 4) {
         inc += 2;
         cnt = 0;
         len += 2;
      }
   }
   cout << len << endl;
   exit(EXIT_SUCCESS);
}
