/*#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

typedef struct {
	char ime[20];
	char prezime[20];
	unsigned razred;
	unsigned odeljenje;
} ucenik;

void citaj(ucenik* u) {
	printf("Unesi ime : ");
	gets(u->ime);
	printf("Unesi prezime : ");
	gets(u->prezime);
	printf("Unesi razred : ");
	scanf("%u", &u->razred);
	printf("Unesi odeljenje : ");
	scanf("%u", &u->odeljenje);
}

int main() {
	ucenik x;
	int n = 3, i;
	FILE* f;
	f = fopen("fajl.txt", "w");

	//printf("Unesite broj ucenika");
	//scanf("%d", &n);
	while (getchar() != '\n')
	{
		

		for (i = 0; i < n; i++) {
			printf("Unesite podatke za %d.", i + 1);
			citaj(&x);
			fprintf(f, "%s %s %u %u", x.ime, x.prezime, x.prezime, x.razred);
		}
	}
	return 0;
}*/