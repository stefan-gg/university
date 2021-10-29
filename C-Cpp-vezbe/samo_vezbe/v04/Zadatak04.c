/*#include <stdio.h>
#define _CRT_SECURE_NO_WARNNGS

int zbir(int* a, int* b) {
	return *a + *b;
}

int razlika(int* a, int* b) {
	return *a - *b;
}


int main() {
	int a = 10, b = 5, zbirr, razlikaa;
	//niz pokazivaca na f-je od 2
	int (*pointer[2])(int*, int*) = {zbir, razlika};
	pointer[0] = zbir;
	pointer[1] = razlika;

	zbirr = (*pointer[0])(&a, &b);
	razlikaa = (*pointer[1])(&a, &b);




	return 0;
}*/