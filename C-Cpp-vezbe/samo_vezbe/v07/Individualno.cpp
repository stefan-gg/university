/*#include <iostream>
using namespace std;
void dupliranje(int& a);
void razlikaZbir(const int& a,const int& b, int& razlika, int& zbir);

int main() {
	int aa = 10;
	int& b = aa;
	int& c = aa;
	//int& a = b;

	int zbir = 0;
	int razlika = 0;

	int& razlikaa = razlika;
	int& zbirr = zbir;

	razlikaZbir(c, b, razlikaa, zbirr);

	//dupliranje(a);

	cout << zbirr << endl;
	cout << razlikaa << endl;

	return 0;
}

void dupliranje(int& a) {
	a *= 2;
}

void razlikaZbir(const int& a,const int& b,int& razlika,int& zbir) {
	 zbir = a + b;
	 razlika = a - b;
}*/