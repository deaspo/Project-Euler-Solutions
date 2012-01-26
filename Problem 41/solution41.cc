#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool isPrime(unsigned long long num);
int toInt(const int *num, int size);

int main(void) {
   vector<int> permutations;
   int a[] = {1, 2, 3, 4, 5, 6, 7};
   int i, size = 7, largest = 0;

   do
      permutations.push_back(toInt(a, size));
   while (next_permutation(a, a + size));
   
   for (i = 0; i < permutations.size(); i++)
      if (permutations[i] > largest)
         if (isPrime(permutations[i]))
            largest = permutations[i];

   cout << largest << endl;
   return 0;
}

bool isPrime(unsigned long long num) {
   bool prime = true;
   if (num == 2 or num == 3);
   else if (num % 2 == 0 or num % 3 == 0)
      prime = false;
   else {
      for (unsigned long long k = 6; (k - 1)*(k - 1) <= num and prime; k += 6)
         if (num % (k - 1) == 0 or num % (k + 1) == 0)
            prime = false;
   }
   return prime;
}

int toInt(const int *num, int size) {
   unsigned n = 0, p = 1, i;
   for (i = 0; i < size; i++) {
      n += num[i]*p;
      p *= 10;
   }
   return n;
}

