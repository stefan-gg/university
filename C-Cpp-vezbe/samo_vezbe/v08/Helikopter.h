#pragma once
#include <iostream>
using namespace std;

class Helikopter {
public:
	void setRegistarskiBroj(int registarskiBroj) {
		this->registarskiBroj = registarskiBroj;
	};

	int getRegistarskiBroj() {
		return this->registarskiBroj;
	};

	void setMaksimalnaBrzina(int masksimalnaBrzina) {
		this->maksimalnaBrzina = masksimalnaBrzina;
	};

	int getMaksimalnaBrzina() {
		return this->maksimalnaBrzina;
	};

	void setBrojSedista(int brojSedista) {
		this->brojSedista = brojSedista;
	};

	int getBrojSedista() {
		return this->brojSedista;
	};
	Helikopter();
	~Helikopter();
private :
	int registarskiBroj;
	int maksimalnaBrzina;
	int brojSedista;
};