#include <iostream>
#include <vector>
#define LIMIT 40586
using namespace std;

void toVector(vector<char>& num, int n) {
   while (n > 0) {
      num.push_back(n % 10);
      n /= 10;
   }
}

unsigned fac(unsigned num) {
   unsigned prod = 1;
   if (num > 0) {
      for (int i = 2; i <= num; i++)
         prod *= i;
   }
   return prod;
}

unsigned facSum(const vector<char>& num) {
   unsigned sum = 0;
   for (unsigned i = 0; i < num.size(); i++)
      sum += fac(num[i]);
   return sum;
}

int main() {
   unsigned i, j, sum = 0;
   vector<char> num;
   for (i = 3; i < LIMIT; i++) {
      toVector(num, i);
      if (facSum(num) == i)
         sum += i;
      num.clear();
   }
   cout << sum << endl;
   exit(EXIT_SUCCESS);
}
