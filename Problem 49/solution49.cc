#include <iostream>
#include <vector>

using namespace std;
vector<int> v1, v2;
bool isPermutation(unsigned m, unsigned n);
void toVector(vector<int>& num, int n);
bool isPrime(unsigned num);

int main(void) {
   unsigned i;
   bool found = false;
   for (i = 1489; !found; i += 2) {
      if (isPrime(i))
         if (isPermutation(i, i + 3330))
            if (isPermutation(i, i + 6660))
               if (isPrime(i + 3330))
                  if (isPrime(i + 6660))
                     found = true;
   }
   cout << i - 2 << i + 3328 << i + 6658 << endl;
   return 0;
}

bool isPermutation(unsigned m, unsigned n) {
   toVector(v1, m);
   toVector(v2, n);
   bool found;
   unsigned size = v1.size(), cnt = 0;
   if (size == v2.size()) {
      for (int i = 0; i < size; i++) {
         found = false;
         for (int j = 0; j < size and !found; j++) {
            if (v1[i] == v2[j]) {
               cnt++;
               v2[j] = -1; // Make sure it isn't selected again
               found = true;
            }
         }
      }
   }
   return (cnt == size) ? true : false;
}

void toVector(vector<int>& num, int n) {
   num.clear();
   while (n > 0) {
      num.push_back(n % 10);
      n /= 10;
   }
}

bool isPrime(unsigned num) {
   bool prime = true;
   if (num == 2 or num == 3);
   else if (num % 2 == 0 or num % 3 == 0)
      prime = false;
   else {
      for (int k = 6; (k - 1)*(k - 1) <= num and prime; k += 6)
         if (num % (k - 1) == 0 or num % (k + 1) == 0)
            prime = false;
   }
   return prime;
}

