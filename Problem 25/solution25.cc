#include <iostream>
#include "../../Integer/Integer.h"

using namespace std;

int main() {
   Integer a(1), b(1), term(2);
   unsigned int limit = 1000;
   unsigned long long cnt = 3;
   while (term.getSize() < limit) {
      a = b;
      b = term;
      term = a + b;
      cnt++;
   }
   cout << "Term number " << cnt << " is the first to have " << limit << " digits." << endl;

   return EXIT_SUCCESS;
}
