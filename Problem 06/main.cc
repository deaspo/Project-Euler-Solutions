#include <iostream>
#include <cmath>
using namespace std;

int main(void) {
	double sum1 = 0.0;
	double sum2 = 0.0;
	for (double i = 1.0; i <= 100.0; i++) {
		sum1 += i;
		sum2 += pow(i,2.0);
	}
	cout << "The difference is " << (int)(pow(sum1,2.0) - sum2) << endl;
}
