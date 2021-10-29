#include <stdio.h>
#define PROM 100
#define kvadrat(a) a * a

int main() {
	int a[PROM];
	/*
#ifdef PROM
	printf("");
#endif*/ 
//#undef PROM
//#ifdef PROM 500

	int a = 5;
	printf("%d", kvadrat(a + 2));

	return 0;
}
