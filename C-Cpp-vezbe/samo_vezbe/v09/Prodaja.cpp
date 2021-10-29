#include "Prodaja.h"
#include <iostream>
using namespace std;

Prodaja::Prodaja() {
	for (int i = 0;i < 12; i++) {
		prodajaPoMesecima[i] = 0;
	}
}

void Prodaja::unesiProdaje() {
	double prodaja;
	for (int i = 0;i < 12; i++) {
		cout << "Unesite kolicinu prodaje za mesec" << i + 1;
		cin >> prodaja;
		setProdaja(i, prodaja);
	}
}

void Prodaja::setProdaja(int i, double p) {
	if (i >= 0 && i < 12 && p > 0) {
		prodajaPoMesecima[i] = p;
	}
	else {
		cout << "Nevazeca" << endl;
	}
}

void Prodaja::stampanjeProdaje() {
	cout << ukupnaGodProdaja();
}

double Prodaja::ukupnaGodProdaja() {
	double suma = 0.0;
	for (int i = 0;i < 12; i++) {
		suma += prodajaPoMesecima[i];
	}
	return suma;
}

double& Prodaja::operator[](int i) {
	return prodajaPoMesecima[i];
}
