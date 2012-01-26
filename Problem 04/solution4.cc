#include <iostream>
#include <string>
#include <sstream>

using namespace std;
bool isPalindrome(const string& s);

int main(void) {
   int i, j, prod, best;
   string str;
   stringstream ss;
   best = 0;
   for (i = 999; i >= 100; i--) {
      for (j = 999; j >= 100; j--) {
         prod = i*j;
         ss << prod;
         ss >> str;
         ss.clear();
         if (isPalindrome(str) and (prod > best)) {
            best = prod;
            cout << "Palindrome found: " << prod << endl;
         }
      }
   }

   return 0;
}

bool isPalindrome(const string& s) {
   bool result = true;
   int size = s.size();
   int j = size - 1;
   
   for (int i = 0; i <= j; i++) {
      if (s[i] != s[j])
         result = false;      
      j--;
   }
   
   return result;
}
