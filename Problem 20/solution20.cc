#include <iostream>
#include <vector>
#include "../../Integer/Integer.h"

using namespace std;

int main() {
   Integer n = 1;
   int limit = 100;
   int sum = 0;
   vector<char> nBody;

   for (int i = 1; i <= limit; i++)
      n *= i;

   cout << limit << "! = " << n << endl;
   n.getBody(nBody);

   for (int i = 0; i < n.getSize(); i++)
      sum += nBody[i];

   cout << "The sum of digits is " << sum << endl;
   return EXIT_SUCCESS;
}
