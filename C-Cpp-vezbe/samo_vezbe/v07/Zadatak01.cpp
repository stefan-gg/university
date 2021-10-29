#include <iostream>

using namespace std;

int kvadriranjePoVrednosti(int x);
void kvadriranjePoRefernci(int& a);
void kvadriranjePoReferncii(int* a);

int main() {

	int x = 5;
	int& y = x;

	x = 7;
	y = 3;
	//ako se x ili y promeni menja se vrednost
	int p = kvadriranjePoVrednosti(x);
	cout << p << endl;
	cout << x << endl;
	cout << y;

	kvadriranjePoRefernci(y);

	return 0;
}

int kvadriranjePoVrednosti(int x) {
	x = x * x;
	return x;
}

void kvadriranjePoReferncii(int* a) {
	*a = *a * *a;
}

void kvadriranjePoRefernci(int& a) {
	a = a * a;
}

inline int kvadriranje(int x = 1) {
	return x * x;
}
