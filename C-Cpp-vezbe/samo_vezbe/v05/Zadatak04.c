#include <stdio.h>
#include <stdlib.h>



void main() {

	int i, n;
	int* ptr, ptr2;

	printf("Unesite velicinu niza");
	scanf("%d", &n);

	ptr = (int*)calloc(n, n*sizeof(int));

	//ptr = (int*)malloc(n * sizeof(int));

	/*if (ptr == NULL) {
		printf("Ops! Mistakes were made");
	}*/
	for (i = 0; i < n; i++) {
		printf("Opala");
		scanf("%d", &ptr[i]);
	}

	n = 21;
	//napravi novi pokazivac za realloc i unistava pointer
	ptr2 = (int*)realloc(ptr, n * sizeof(int));
	if (ptr2 == NULL) {
		printf("Ops! Mistakes were made");
		exit(1);
	}

	free(ptr);
	free(ptr2);
}