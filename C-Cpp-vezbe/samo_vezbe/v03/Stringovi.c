#include <stdio.h>
#define MAX 50

//ovo Je Prva recenica. Ovo je druGA
// isspace(znak);
int main() {
	
	char str[100]; // '\0'
	enum {F, T};
	int znak, i;
	int znak, prvi = T;
	/*
	while ((znak = getchar()) != EOF) {
		if (isupper(znak)) {
			if (!prvi) {
				znak = tolower(znak);
			}
		}
		else if (islower(znak))
		{
			if (prvi) {
				znak = toupper(znak);
				prvi = F;
			}
		}
		else
		{
			if (znak == '.' || znak == '!' || znak == '?')
				prvi = T;
		}
		putchar(znak);
	}
	*/


	// ******************************************************
	/*
	while ((znak = getchar()) != EOF) {
		if (!isspace(znak)) {
			str[i] = znak;
			i++;
		}
	}

	str[i] = '\0';
	printf("%s", str);
	*/

	char prviString[MAX];
	char drugiString[MAX];

	printf("Unesite prvi string \n");
	gets(prviString);
	printf("Unesite drugi string \n");
	gets(drugiString);
	
	// 0 - isti  

	if (!strcmp(prviString, drugiString)) {
		printf("Isti su");
	}
	else {
		printf("Nisu isti");
	}
	
	strcpy(prviString, drugiString);
	printf("%s\n", prviString);

	strcat(prviString, drugiString);
	gets(prviString);

	return 0;
}