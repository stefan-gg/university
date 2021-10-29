#pragma once
#include <iostream>
using namespace std;

class Kompleksni
{
protected:
	int real, imag;
public:
	Kompleksni(int r, int i): real(r), imag(i) {}

	friend ostream& operator<<(ostream& out, const Kompleksni a);
	bool operator>(const Kompleksni& k); /*{
		if (this->real > k.real) {
			return true;
		}
		else if (this->real == k.real) {
			if (this->imag > k.imag)
				return true;
		}
		return false;
	}*/
};

