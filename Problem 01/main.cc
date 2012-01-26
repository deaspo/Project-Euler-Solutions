#include <iostream>
using namespace std;

int main(void) {
	int number;
	int sum = 0;
	for (number = 1; number < 1000; number++) {
		if (((number % 3) == 0) or ((number % 5) == 0)) {
			sum += number;
			cout << number << " ";
		}
	}
	cout << "= " << sum << endl;
}
