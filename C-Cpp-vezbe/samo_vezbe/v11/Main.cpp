#include "Oblik.h"

int main() {

	/*Trougao t;
	Pravougaonik p;

	Oblik* ot = &t;
	Oblik* op = &p;

	ot->podesiVrednosti(12, 3);
	op->podesiVrednosti(12, 3);*/

	Oblik* op = new Trougao(3, 4);
	Oblik* ot = new Pravougaonik(3, 4);

	Oblik* niz[4];

	for (int i = 0; i < 4;i++) {
		if (i % 2 == 0)
			niz[i] = new Trougao(3, 4);
		else
			niz[i] = new Pravougaonik(3, 4);
	}

	for (int i = 0; i < 4;i++) {
		cout << niz[i]->povrsina() << endl;
	}

	for (int i = 0; i < 4;i++) {
		delete niz[i];
	}
	//jer svaki element se dinamicki kreira
	delete[] niz;

	return 0;
}