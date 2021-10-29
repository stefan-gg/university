#pragma once
#include <iostream>
using namespace std;

class Artikal
{
protected:
	string ime;
	int cena;
public:
	Artikal() {}
	virtual ~Artikal() {}
	Artikal(string ime, int c):ime(ime), cena(c){}
	//f-ja mora, ne setter
	/*void setCena(int c) {
		this->cena = c + (c * 0.8);
	}*/
	virtual float odrediPdv() = 0;
};

class Tehnika : public Artikal
{
private:

public:
	Tehnika() {}
	Tehnika(string ime, int c) : Artikal(ime, c) {};
	
	float odrediPdv() {
		return 0.20 * cena + cena;
	}

	virtual ~Tehnika() {}
	
	
};

class Netehnicka : public Artikal
{
private:

public:
	Netehnicka() {}
	Netehnicka(string ime, int c) : Artikal(ime, c) {};

	float odrediPdv() {
		return 0.08 * cena + cena;
	}

	virtual ~Netehnicka() {}


};
