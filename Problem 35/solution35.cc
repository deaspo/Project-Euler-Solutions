#include <iostream>
#include <cmath>
#include <deque>
using namespace std;

void toDeque(deque<int>& num, int n) {
   num.clear();
   while (n > 0) {
      num.push_back(n % 10);
      n /= 10;
   }
}

unsigned toInt(const deque<int>& num) {
   unsigned n = 0, p = 1;
   for (int i = 0; i < num.size(); i++) {
      n += num[i]*p;
      p *= 10;
   }
   return n;
}

bool isPrime(unsigned num) {
   bool prime = true;
   for (int i = 2; i <= sqrt(num) and prime; i++)
      if (num % i == 0)
         prime = false;
   return prime;
}

bool isCircularPrime(deque<int>& num) {
   int tmp;
   bool prime = true;
   for (int i = 0; i < num.size() and prime; i++) {
      if (!isPrime(toInt(num)))
         prime = false;
      tmp = num.front();
      num.pop_front();
      num.push_back(tmp);
   }
   return prime;
}

int main() {
   unsigned i, j, sum = 5;
   deque<int> num;
   for (i = 13; i < 1000000; i += 2) {
      toDeque(num, i);
      if (isCircularPrime(num))
         sum++;
   }
   cout << sum << endl;
   exit(EXIT_SUCCESS);
}
