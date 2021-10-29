#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main() {
	/*
	int i = 0;
	int niz[5] = {1, 2, 3, 4, 5};
	int* p_niz;
	p_niz = niz;
	p_niz = &niz[2];
	
	//niz[0] = niz[2] + niz[4]
	*(p_niz - 2) = *(p_niz) + *(p_niz + 2);

	//printf("%d", *(p_niz + 2));
	for (i = 0;i < 5; i++) {
		printf("%d", niz[i]);
	}

	for ( i = 0; i < 5; i++)
	{
		printf("%d", *(p_niz + i));
	}*/
	
	int i = 0;
	char tekst[] = {"Ovo je niz \n"};
	char* p_tekst = tekst;

	for (i = 0;tekst[i] != '\0';i++) {
		putchar(tekst[i]);
	}

	for (; *p_tekst != '\0'; p_tekst++) {
		putchar(*p_tekst);
	}

	return 0;
}




