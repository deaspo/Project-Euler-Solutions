#include <iostream>

using namespace std;

bool isPrime(int number);

int main(void) {
   bool found = false;
   bool finished;
   int number = 3;
   int prime = 2;
   int power = 1;
   while(!found) {                              // For each odd composite
      if(!isPrime(number)) {
         // Find a prime number
         prime = 2;
         finished = false;
         while((prime < number) && !finished && !found) {      // For each prime
            finished = false;
            while(!finished) {
               if(isPrime(prime)) {
                  finished = true;
               }
               else {
                  prime = prime + 1;
               }
            }
            power = 1;
            finished = false;
            while((number >= (prime + 2 * power * power)) && !finished) {       // For each power
               if(number == (prime + 2 * power * power)) {
                  finished = true;
                  cout << number << " = " << prime << " + 2*" << power << "^2" << endl;
               }
               else {
                  power = power + 1;
               }   
            }

            if(prime > number) {
               found = true;
               cout << "The first number that can not be written as the sum of a prime " <<
                       "and twice a square is " << number << "." << endl;
            }
            else {
               prime = prime + 1;
            }
         }
      }
      number = number + 2; // Try next odd number
   }

	return EXIT_SUCCESS;
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
