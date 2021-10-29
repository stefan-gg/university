#include "Complex.h"
#include <iostream>
using namespace std;
int main() {

	Complex a(50, 40), b(10, 20);
	//interno a.operat-(b)
	//prijateljska operator-(a,b)
	//opetatori mogu i fje clanice i prijateljske
	Complex c = a + b;

	if (b < a) {
		cout << "true";
	}
	else {
		cout << "false";
	}
	/*Complex*/ c = a - b;
	cout << c.getReal() << " + " << c.getImag() << "i";

	return 0;
}