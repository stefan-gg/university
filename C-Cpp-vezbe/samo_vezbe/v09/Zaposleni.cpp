#include "Zaposleni.h"
#include <iostream>
using namespace std;
#include <cstring>

int Zaposleni::brojac = 0;

Zaposleni::Zaposleni(const char* i, const char* p) {
	ime = new char[strlen(i) + 1];
	strcpy(ime, i);

	prezime = new char[strlen(p) + 1];
	strcpy(prezime, p);

	brojac++;
	cout << "Konstruktor pozvan" << endl;
}

Zaposleni::~Zaposleni() {
	delete[] ime;
	delete[] prezime;

	cout << "Destruktor pozvan";
	brojac--;
}

int Zaposleni::getBrojac() {
	return brojac;
}