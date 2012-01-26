#include <iostream>
#include <cmath>

using namespace std;
int d(int);

int main() {
   int sum = 0, i, j, k;
   int limit = 100000;
   for (i = 1; i < limit; i++) {
      j = d(i);
      k = d(j);
      sum += (i != j and i == k) ? i : 0;
   }
   cout << sum << endl;
   return EXIT_SUCCESS;
}

int d(int num) {
   int i, sum = 1, limit = (int)sqrt(num);
   for (i = 2; i <= limit; i++)
      if (num % i == 0)
         sum += (i == num/i) ? i : i + num/i;
   return sum;
}
