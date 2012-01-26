#include <iostream>
#define MAX_SIZE 2400
using namespace std;

bool isPentagonal(unsigned long long* list, unsigned long long n, unsigned int beg) {
   bool pentagonal = false;
   for (int i = beg; i < MAX_SIZE and list[i] <= n and !pentagonal; i++)
      if (list[i] == n)
         pentagonal = true;
   return pentagonal;
}

int main() {
   unsigned int i, j, size = 0;
   unsigned long long diff, list[MAX_SIZE];
   bool found = false;

   for (i = 1; i < MAX_SIZE; i++)
      list[i - 1] = i*(3*i - 1)/2;
   for (i = 0; i < MAX_SIZE and !found; i++)
      for (j = 0; j < i and list[i] + list[j] <= list[MAX_SIZE - 1] and !found; j++)
         if (isPentagonal(list, list[i] + list[j], i))
            if (isPentagonal(list, list[i] - list[j], i - j)) {
               found = true;
               diff = list[i] - list[j];
            }

   cout << diff << endl;
   exit(EXIT_SUCCESS);
}
