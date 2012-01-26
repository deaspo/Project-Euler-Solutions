#include <vector>
#include <cmath>

using namespace std;

/* Function generates prime numbers up to num using Sieve's algorithm */
vector<unsigned> generatePrimes(unsigned limit);

/* Function returns true if num is a prime number */
bool isPrime(unsigned);

/* Function returns the sum of coprimes (<n) to n */
unsigned int phi(unsigned);

/* Converts an int n to vector num, 345 -> [3,4,5]*/
void toVector(vector<int>&, int);

/* Converts a vector num to an int, [3,4,5] -> 345 */
unsigned toInt(const vector<int>&);

/* Checks wether a number is abundant */
bool isAbundant(int);

/* Returns the sum of all divisors to num */
int sumOfDivisors(int);

/* Returns the greatest common divisor of a and b */
int gcd(int a, int b);

/* Returns true if m and n are permutations of each others */
bool isPermutation(unsigned m, unsigned n);
