#pragma once
#include <iostream>
using namespace std;

class Osnovna
{
private:
	int podatak;
protected:
	int getPodatak() { return podatak; }

public:
	void prikazi(){ cout << "Osnovna klasa" << endl; }
};

