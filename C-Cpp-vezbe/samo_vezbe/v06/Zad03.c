/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define MAX_DUZINA 100
#define MAX_VELICINA 100000

int main(int argc, char* argv[]) {

    char u_dat[MAX_DUZINA];
    char i_dat[MAX_DUZINA];
    char ch;
    char prostor[MAX_VELICINA];
    int br = 0;
    FILE* p_ulazna, * p_izlazna;

    printf("Unesite naziv ulazne datoteke ");
    scanf("%s", u_dat);

    p_ulazna = fopen(u_dat, "r");
    if (p_ulazna == NULL)
    {
        printf("Greska pri otvaranju datoteke");
        return 1;
    }

    if (strcmp(u_dat, i_dat) == 0)
    {
        printf("Najeb jer su oba ista");
        return 1;
    }

    p_izlazna = fopen(i_dat, "w");
    if (p_izlazna == NULL) {
        printf("Najeb na izlazu");
    }

    while ((ch = fgetc(p_ulazna)) != EOF)
    {
        prostor[br++] = ch;
    }
    if (br == 0) {
        printf("Prazan najeb");
        return 0;
    }

    int i = 0;
    prostor[i] = toupper(prostor[i]);
    fprintf(p_izlazna, "%c", prostor[i]);

    for (i = 0; i < br; i++)
    {
        if (islower(prostor[i])) {
            if (!isalpha(prostor[i - 1])) {
                prostor[i] = toupper(prostor[i]);
            }
        }
        if (isupper(prostor[i])) {
            if (!isalpha(prostor[i - 1])) {
                prostor[i] = tolower(prostor[i]);
            }
        }
        fprintf(i_dat, "%c", prostor[i]);
    }
    fclose(i_dat);
    fclose(u_dat);

    return 0;
}*/