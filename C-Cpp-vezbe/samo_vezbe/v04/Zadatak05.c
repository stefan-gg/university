/*#include <stdio.h>
#define _CRT_SECURE_NO_WARNNGS
//kopiranje String sa pokazivacima
void copy1(char* s1, char* s2) {

	int i;
	for (i = 0; (s1[i] = s2[i]) != '\0'; i++);
}

void copy2(char* s1, char* s2) {
	for (; (*s1 = *s2) != '\0'; s1++, s2++);
}

int main() {

	char string1[10];
	char* string2 = "Zdravo";

	copy1(string1, string2);
	copy2(string1, string2);


	return 0;
}*/