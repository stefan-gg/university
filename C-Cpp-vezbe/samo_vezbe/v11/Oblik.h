#pragma once
#include <iostream>
using namespace std;

class Oblik
{
protected:
	int visina, sirina;

public:
	Oblik() {}
	
	Oblik(int s, int v): sirina(s), visina(v){}

	virtual ~Oblik() { cout << "Destruktor oblik" << endl; }
	
	void podesiVrednosti(int s, int v) {
		visina = v;
		sirina = s;
	}
	//znaci da treba da je predefinisu u izvedene
	/*virtual int povrsina() {
		return 0;
	}*/
	virtual int povrsina() = 0;
};

//protected ostaje protected,  samo se moze smanji ne moze se poveca privatn
class Trougao : public Oblik {

public:
	Trougao() {}
	Trougao(int s, int v) :Oblik(s, v) {}
	virtual ~Trougao() { cout << "Destruktor trougao" << endl; }
	int povrsina() {
		return (sirina * visina) / 2;
	}
};

class Pravougaonik : public Oblik {
public:
	Pravougaonik(int s, int v) :Oblik(s, v) {}
	int povrsina() {
		return visina * sirina;
	}
};

