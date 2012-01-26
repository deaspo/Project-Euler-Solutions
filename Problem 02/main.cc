#include <iostream>

using namespace std;

int main(void) {
	int sum = 0;
	int current = 0;
	int prev1 = 1;
	int prev2 = 1;
	while (current < 1000000) {
		current = prev1 + prev2;
		if (current % 2 == 0)
			sum += current;
		prev2 = prev1;
		prev1 = current;
	}
	cout <<  "Sum is " << sum << endl;
}
