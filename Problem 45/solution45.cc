#include <iostream>

using namespace std;

int main(void) {
   bool found = false;
   unsigned int T_n, P_m, H_k, n, m, k;
   n = 285;
   while (!found) {
      n += 1;
      T_n = n*(n + 1)/2;
      P_m = m = 0;
      while (P_m < T_n) {
         m += 1;
         P_m = m*(3*m - 1)/2;
      }
      if (P_m == T_n) {
         H_k = k = 0;
         while (H_k < P_m) {
            k += 1;
            H_k = k*(2*k - 1);
         }
         if (H_k == P_m)
            found = true;
      }
   }
   cout << T_n << endl;
   return 0;
}
