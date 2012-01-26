#include <iostream>
#include "../../Integer/Integer.h"

using namespace std;

int main() {
   Integer prod = 1;
   vector<char> prodBody;
   int i, j, sum = 0;

   for (i = 1; i <= 1000; i++) {
      prod *= 2;
   }
   prod.getBody(prodBody);
   for (j = 0; j < prod.getSize(); j++)
      sum += prodBody[j];
   cout << "The sum of digits in 2^" << i - 1 << " is " << sum << endl;

   return EXIT_SUCCESS;
}
