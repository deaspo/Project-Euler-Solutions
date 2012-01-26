#include <iostream>
#include <vector>
#include <cmath>
#define MAX 444000
using namespace std;

void toVector(vector<unsigned>& num, int n) {
   num.clear();
   while (n > 0) {
      num.push_back(n % 10);
      n /= 10;
   }
}

int main() {
   vector<unsigned> v;
   unsigned sum, n, k, ans = 0;
   for (n = 2; n < MAX; n++) {
      sum = 0;
      toVector(v, n);
      for (k = 0; k < v.size(); k++)
         sum += v[k]*v[k]*v[k]*v[k]*v[k];
      if (sum == n)
         ans += n;
   }
   cout << ans << endl;
   exit(EXIT_SUCCESS);
}
