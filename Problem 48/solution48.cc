#include <iostream>
#include "../../Integer/Integer.h"

using namespace std;

int main(int argc, char **argv) {
   Integer sum, num;

   for (int i = 1; i <= atoi(argv[1]); i++) {
      num = i;
      for (int j = 1; j < i; j++) {
         num *= i;
      }
      sum += num;
   }
   
   cout << endl << sum << endl;
   return EXIT_SUCCESS;
}
