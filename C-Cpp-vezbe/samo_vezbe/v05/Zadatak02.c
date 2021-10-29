#include <stdio.h>
#include <math.h>

typedef struct {
	int element1;
	float element2;
	float* p_el2;
} Test;


int main() {

	Test lista1, lista2;
	Test* p_lista;

	lista1.element1 = 5;

	lista1.p_el2 = &lista1.element2;
	*lista1.p_el2 = 4;//preko * postavljamo vrednost

	p_lista = &lista2;
	//(*p_lista).element1 = 7; moze i tako al '->' bolje
	p_lista->element1 = 9;
	p_lista->p_el2 = &p_lista->element2;
	//p_lista->p_el2 =*(p_lista).element2;

	*p_lista->p_el2 = 90.32;


	return 0;
}