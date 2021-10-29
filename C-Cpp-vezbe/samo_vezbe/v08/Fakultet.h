#pragma once
#include <iostream>
using namespace std;

class Fakultet{

public:
	char adresa[30];
	int brZaposlenih;

	void info();
	void infoZarada();

	float getZarada() {
		return this->zarada;
	};

	void setZarada(float zarada) {
		this->zarada = zarada;
	};

private:
	float zarada;

};


