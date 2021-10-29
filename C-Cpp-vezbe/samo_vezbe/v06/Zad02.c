/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MAX_LINE 256

//a.exe ulazna.txt izlazna.txt
int main(int argc, char* argv[]) {

	char line[MAX_LINE];
	FILE* in, * out;
	int line_num;

	if (argc != 3) {
		fprintf(stderr, "Upotreba: %s ulazna izlazna", argv[0]);
		return 1;
	}

	in = fopen(argv[1], "r");
	if (in == NULL) {
		fprintf(stderr, "Greska");
		return 1;
	}

	out = fopen(argv[2], "w");
	if (out == NULL) {
		fprintf(stderr, "Greska");
		return 1;
	}

	line_num = 1;
	while (fgets(line, MAX_LINE, in) != NULL) {
		fprintf(out, "%d. ", line_num++);
		fputs(line, out);
	}

	fclose(in);
	fclose(out);

	return 0;
}*/