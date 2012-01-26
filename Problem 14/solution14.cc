#include <iostream>

using namespace std;

int main() {
   unsigned long long cnt = 0;
   unsigned long long num, best = 0;
   for (int i = 1; i < 1000000; i++) {
      cnt = 1;
      num = i;
      while (num != 1) {
         if (num % 2 == 0)
            num /= 2;
         else
            num = 3*num + 1;
         cnt++;
      }
      if (cnt > best) {
         best = cnt;
         cout << "Number " << i << " gave a " << cnt << " number sequence" << endl;
      }
   }
   return EXIT_SUCCESS;
}
