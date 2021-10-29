#pragma once

class Pravougaonik {
	int sirina, visina;
	
public:
	char* boja;
	
	Pravougaonik();
	Pravougaonik(int s, int v);
	Pravougaonik(int s, int v, char* boja);

	//konstruktor kopije 
	Pravougaonik(const Pravougaonik &p);

	~Pravougaonik();
	// po vrednosti, vrednosti p su proslednjene

	int povrsina() {
		return sirina * visina;
	}

	int obim() {
		return (2 * sirina) + (2 * visina);
	}
};
