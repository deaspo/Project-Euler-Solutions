#include <iostream>
using namespace std;
int main() {
   unsigned sum = 1, num = 3, inc = 2, cnt = 1;
   while (num <= 1001*1001) {
      sum += num;
      num += inc;
      cnt += 1;
      if (cnt == 4) {
         inc += 2;
         cnt = 0;
      }
   }
   cout << sum << endl;
   exit(EXIT_SUCCESS);
}
