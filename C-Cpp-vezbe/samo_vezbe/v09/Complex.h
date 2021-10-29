#pragma once
#include <ostream>
class Complex
{
	float real, imag;

public:
	Complex() :real(0), imag(0) {};
	Complex(float r, float i) :real(r), imag(i) {};

	float getReal() {
		return real;
	}

	void setReal(float r) {
		real = r;
	}
	float getImag() {
		return imag;
	}
	void setImag(float i) {
		imag = i;
	}

	Complex operator+(const Complex& b);
	friend Complex operator-(const Complex& a, const Complex& b);

	bool operator<(const Complex& b);
	friend bool operator<(const Complex& a, const Complex& b);
	//int operator<(const Complex& b);
	//friend int operator<(const Complex& a, const Complex& b);
	//friend ostream& operator<<(ostream& out, const Complex& b);
	//friend ostream& operator>>(istream& in, Complex& b);
};

