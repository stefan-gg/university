#include <stdio.h>
#include <stdlib.h>


int* kreirajNiz(int n) {
	return (int*)malloc(n * sizeof(int));
}

int* unosNiza(int n) {
	int i;
	int* x = kreirajNiz(n);
	for (i < 0; i < n; i++) {
		scanf("%d", &x[i]);
	}
	return x;
}

void main() {
	int i, n;
	int* a;

	a = unosNiza(n);

	printf("");
	for (i = 0; i < n; i++) {
		printf("%d", a[i]);
	}

	free(a);
}