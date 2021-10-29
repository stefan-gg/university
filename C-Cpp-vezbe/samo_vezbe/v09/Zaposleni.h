#pragma once
class Zaposleni
{
private:
	char* ime;
	char* prezime;
	static int brojac;

public:
	Zaposleni(const char* i, const char* p);
	~Zaposleni();

	static int getBrojac();
	//prvi znaci da se konstantan pokazivac vraca
	//drugi const da u fji ne menjamo obj
	const char* getIme()const {
		return ime;
	}

	const char* getPrezime()const {
		return prezime;
	}
};

