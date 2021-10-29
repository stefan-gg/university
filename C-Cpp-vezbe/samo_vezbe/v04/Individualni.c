#include <stdio.h>
#include <string.h>
#define _CRT_SECURE_NO_WARNNGS
//1 2 3 8
//zadatak 1
void f1(int* p) {
	*p = *p * 2;
}

void f2(int* p) {
	*p = *p * -1;
}

void f3(int* p, int* a, int* kolicnik, int* ostatak) {
	*kolicnik = *p / *a;
	*ostatak = *p % *a;
}

void f4(int* p, int* a, int* zbir, int* razlika) {
	*zbir = *p + *a;
	*razlika = *p - *a;
}

void f8(int* string, int* ps) {
	for (; (*string == *ps) != '\0'; string++, ps--) {
		
	}
	
}

int palindrom(char* c) {
	for (int i = 0; i < strlen(c); i++)
	{
		if (*(c + i) != *(c + strlen(c) - 1 - i))
		{
			return 0;
		}
	}
	return 1;
}


int main() {
	int a = 77, b = 12, kolicnik, ostatak, zbir, razlika, duzina;
	 
	char* p7 = {"Ovo je string"};
	duzina = strlen(*p7);
	int* p = &a;
	int* p2 = &b;
	int* p3 = &kolicnik;
	int* p4 = &ostatak;
	int* p5 = &zbir;
	int* p6 = &razlika;
	int* p8 = *(p7 + duzina - 1);
	//f1(p);
	//f2(p);
	//f3(p, p2, p3, p4);
	//f4(p, p2, p5, p6);
	palindrom(p7);
	//printf("%d", a);
	//printf("%d \n", zbir);
	//printf("%d \n", razlika);
}