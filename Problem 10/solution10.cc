#include <iostream>
#include <cmath>

using namespace std;
bool isPrime(unsigned int n);

int main(int argc, char **argv) {
   unsigned long long sum, i, roof;
   sum = 2;
   roof = argc > 1 ? atoi(argv[1]): 100;  // Set roof to 100 if no parameter is given
   for (i = 3; i < roof; i += 2) {
      if (isPrime(i))
         sum += i;
   }
   cout << "The sum of all primes below " << roof << " equals " << sum << endl;
   return 0;
}

bool isPrime(unsigned int n) {
   bool result = true;
   unsigned int i, roof = (unsigned int)sqrt((double)n) + 1;
   
   for (i = 2; i <= roof; i++) {
      if (n % i == 0) {
         result = false;
         break;
      }
   }  
   return result;
}
