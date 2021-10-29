#include <stdio.h>
#include "Stringbiblioteka.h"

void string_copy(char dest[], char src[]) {
    int i;
    while (src[i] != '\0') {
        dest[i] = src[i];
        i++;
    }
    dest[i] = '\0';
}

int main() {

	char dest[] = {'a'};
	char src[] = {'a', 'a', 'b'};

	string_copy(dest[2], src[3]);

	return 0;
}

