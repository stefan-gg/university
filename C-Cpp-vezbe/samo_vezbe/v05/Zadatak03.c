#include <stdio.h>

typedef struct {
	char ime[20];
	char prezime[20];
	int brojGodina;
} Osoba;

//Osoba osoba; moze ovo
void stampajOsobu(Osoba* osoba) {
	printf("%s", osoba->ime);
	printf("%s", osoba->prezime);
	printf("%s", osoba->brojGodina);
}

void main(void) {

	Osoba osoba;
	Osoba* p_osoba = &osoba;

	strcpy(osoba.ime, "Nikola");
	strcpy(osoba.prezime, "Nikola");
	osoba.brojGodina = 20;

	stampajOsobu(p_osoba);

	strcpy(p_osoba->ime, "Petar");
	strcpy(p_osoba->ime, "Petarski");
	p_osoba->brojGodina = 30;

}
