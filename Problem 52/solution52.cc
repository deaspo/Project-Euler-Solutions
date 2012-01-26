#include <iostream>
#include <vector>

using namespace std;
vector<int> v1, v2;
bool isPermutation(unsigned m, unsigned n);
void toVector(vector<int>& num, int n);

int main(void) {
   bool found = false;
   unsigned x;
   for (x = 1; !found; x++) {
      if (isPermutation(x, 2*x))
         if (isPermutation(2*x, 3*x))
            if (isPermutation(3*x, 4*x))
               if (isPermutation(4*x, 5*x))
                  found = true;
   }
   cout << x - 1 << endl;
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

