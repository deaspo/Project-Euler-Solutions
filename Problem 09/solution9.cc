#include <iostream>
using namespace std;

void printResults(bool found, unsigned int a, unsigned int b, unsigned int c);

int main() {
   unsigned int a, b, c, sum;
   bool found = false;

   /* Brute forcing this sucker ;-) */
   for (c = 0; !found and (c < 1000); c++) {
      for (b = 0; !found and (b < c); b++) {
         for (a = 0; !found and (a < b); a++) {
            sum = a + b + c;
            if ((sum == 1000) and (a*a + b*b == c*c)) {
               found = true;
               printResults(found, a, b, c);
            }
         }
      }
   }
   if (!found)
      printResults(found, a, b, c);
   return 0;
}

void printResults(bool found, unsigned int a, unsigned int b, unsigned int c) {
   if (found) {
      cout << "Triplet found!" << endl;
      cout << "a = " << a << endl;
      cout << "b = " << b << endl;
      cout << "c = " << c << endl;
      cout << "a + b + c = " << a + b + c << endl;
      cout << "a^2 + b^2 = " << a*a + b*b << " = c^2" << endl;
      cout << "abc = " << a*b*c << endl;
   }
   else {
      cout << "Sorry, but algorithm is incorrect! Results follows:" << endl;
      cout << "a = " << a << endl;
      cout << "b = " << b << endl;
      cout << "c = " << c << endl;
      cout << "a + b + c = " << a + b + c << endl;
      cout << "a^2 + b^2 = " << a*a + b*b << "c^2" << endl;
      cout << "abc = " << a*b*c << endl;

   }   
}
