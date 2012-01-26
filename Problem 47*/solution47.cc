#include <iostream>

using namespace std;

bool isPrime(int number);
bool hasFourDistinctPrimeFactors(int number);

int main(void) {
   bool found = false;
   int number = 0;
   while(!found) {
      number = number + 1;
      if(hasFourDistinctPrimeFactors(number)) {
         if(hasFourDistinctPrimeFactors(number + 1)) {
            if(hasFourDistinctPrimeFactors(number + 2)) {
               if(hasFourDistinctPrimeFactors(number + 3)) {
                  found = true;
               }
            }
         }
      }
   }
   cout << "Answer: " << number << endl;
	return EXIT_SUCCESS;
}

bool hasFourDistinctPrimeFactors(int number) {
   int leftOver = number;
   int factor = 2;
   int numberOfDistinctPrimes = 0;
   int factorProduct = 1;
   while(factorProduct != number) {
      if(isPrime(factor) && (leftOver % factor == 0)) {
         leftOver = leftOver / factor;
         factorProduct = factorProduct * factor;
         numberOfDistinctPrimes = numberOfDistinctPrimes + 1;
         while(leftOver % factor == 0) {
            leftOver = leftOver / factor;
            factorProduct = factorProduct * factor;
         }
      }
      else {
         factor = factor + 1;
      }
   }
   return (numberOfDistinctPrimes == 4);
}

bool isPrime(int number) {
	if(number > 3) {
      for(int i = 2; i * i <= number; i++) {
         if((number % i) == 0) {
            return false;
         }
      }
   }
   else if((number == 2) || (number == 3)) {
      return true;
   }
   else {
      return false;
   }
   return true;
}
