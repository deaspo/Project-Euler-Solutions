#include <iostream>
#include <algorithm>

void permute(int number[], int length);
void swap(int& a, int& b);
using namespace std;

int main(void) {
   int number[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
   int length = 10;

   for(int i = 1; i < 1000000; i++) {
      next_permutation(number, number + length);
   }
   cout << "Answer: ";
   for(int i = 0; i < length; i++) {
      cout << number[i];
   }
   cout << endl;
   return EXIT_SUCCESS;
}
