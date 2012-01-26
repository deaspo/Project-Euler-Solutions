#include <iostream>
#include <cmath>
#define LIMIT 28123
using namespace std;
bool isAbundant(int);

int main() {
   int i, j, k, sum = 0;
   bool abundant[LIMIT + 1], sumOfAbundants[LIMIT + 1] = {false};
   
   for (i = 0; i <= LIMIT; i++)
      abundant[i] = isAbundant(i) ? true : false; 

   for (i = 0; i <= LIMIT; i++)
      for (j = 0; i + j <= LIMIT; j++)
         if (abundant[i] and abundant[j])
            sumOfAbundants[i + j] = true;
   
   for (i = 0; i < LIMIT; i++)
      if (!sumOfAbundants[i])
         sum += i;
   
   cout << sum << endl;
   return EXIT_SUCCESS;
}

bool isAbundant(int num) {
   int i, sum = 0, limit = (int)sqrt(num);
   for (i = 1; i <= limit; i++)
      if (num % i == 0)
         sum += (i == num/i) ? i : i + num/i;
   return (sum > 2*num) ? true : false;
}
