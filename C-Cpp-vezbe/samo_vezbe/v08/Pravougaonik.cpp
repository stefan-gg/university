#include "Pravougaonik.h"
#include <iostream>

Pravougaonik::Pravougaonik() {
	sirina = 5;
	visina = 5;
	boja = new char[10];
}

Pravougaonik::Pravougaonik(int s, int v) : sirina(s), visina(v) {
}

//******
Pravougaonik::Pravougaonik(int s, int v, char* b): sirina(s), visina(v) {
	boja = new char[10];
	strcpy(boja, b);
}



Pravougaonik::~Pravougaonik(){
	delete[] boja;
}

/*int povrsina() {
	return v * ;
}*/

Pravougaonik::Pravougaonik(const Pravougaonik& p) {
	sirina = p.visina;
	boja = new char[10];
	strcpy(boja, p.boja);
}
