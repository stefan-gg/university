#include <stdio.h>
#define _CRT_SECURE_NO_WARNNGS
/*
int duzina(char* p_string) {
	int l = 0;
	char* p = p_string;

	while (*p != '\0')
	{
		l++;
		p++;
	}
	return l;
}*/

// 2 promljenive pozove funkc zameni mesta

void zamenaMesta(int* a, int* b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

int main() {
	/*
	char* tekst = {"Ovo je tekst\n"};
	int i = duzina(tekst);
	printf("Duzina je : %d", i);*/

	int a = 5, b = 100;
	int* aa = &a, bb = &b;
	zamenaMesta(&a, &b);
	printf("a : %d  b : %d", a, b);
	return 0;
}