#include <iostream>
#include <cmath>

using namespace std;
bool isPrime(unsigned int n);

int main(int argc, char **argv) {
   int cnt = 1;
   int prime;
   unsigned int i = 3;
   while (cnt < atoi(argv[1])) {
      if (isPrime(i)) {
         cnt++;
         prime = i;
      }
      i += 2;
   }
   cout << "The " << cnt << "th prime is " << prime << endl;
   return 0;
}

bool isPrime(unsigned int n) {
   bool result = true;
   
   for (unsigned int i = 2; i < n; i++) {
      if (n % i == 0) {
         result = false;
         break;
      }
   }
   
   return result;
}
