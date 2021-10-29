#include <stdio.h>
#define _CRT_SECURE_NO_WARNNGS

int kvadrat(int i) {
	return i * i;
}

int kub(i) {
	return i * i *  i;
}

int paran(int i) {
	return 2 * i;
}

int sumiraj(int (*f)(int), int n) {
	int i, suma = 0;
	for (i = 0;i <= n; i++) {
		suma += (*f)(i);
	}
	return suma;
}

int main() {

	printf("Suma kvadrata od 1 do 3 je %d", sumiraj(&kvadrat, 3));
	printf("Suma kubova od 1 do 3 je %d", sumiraj(&kub, 3));
	printf("Paran broj 2 x veci od 3 je %d", sumiraj(&paran, 1));

	return 0;
}