#include "Complex.h"

Complex Complex::operator+(const Complex& b) {
	Complex c;
	c.real = this->real + b.real;
	c.imag = this->imag + b.imag;
	return c;
}

Complex operator-(const Complex& a, const Complex& b) {
	Complex c;
	c.real = a.real - b.real;
	c.imag = a.imag - b.imag;
	return c;
}

/*int Complex::operator<(const Complex& b) {
	int rezultat;
	Complex c;
	c.real = this->real - b.real;
	c.imag = this->imag - b.imag;
	if (this->real > b.real && this->imag > b.imag) {
		rezultat = 1;
	}
	else if (this->real == b.real && this->imag == b.imag) {
		rezultat = 0;
	}
	else {
		rezultat = -1;
	}
	return rezultat;
}*/

bool  Complex::operator<(const Complex& b) {
	if (this->real < b.real && this->imag < b.imag)
	{
		return true;
	}
	return false;
}

bool operator<(const Complex& a, const Complex& b)
{
	if (a.real < b.real && a.imag < b.imag)
	{
		return true;
	}
	return false;
}

/*int operator<(const Complex& a, const Complex& b) {
	int rezultat;
	Complex c;
	c.real = a.real - b.real;
	c.imag = a.imag - b.imag;
	if (a.real > b.real && a.imag > b.imag) {
		rezultat = 1;
	}
	else if (a.real == b.real && a.imag == b.imag) {
		rezultat = 0;
	}
	else {
		rezultat = -1;
	}
	return rezultat;
}*/
/*ostream& operator<<(ostream& out, const Complex& a) {
	out << a.real << " " << a.imag << "" << endl;
	return out;
}

istream& operator>>(istream& out, Complex& a) {
	in >> a.real >> a.imag;
	return in;
}*/
