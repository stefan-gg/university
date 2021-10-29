#include <iostream>
#include "Fakultet.h"
#include "Pravougaonik.h"
#include "Helikopter.h"

using namespace std;

int main(){
    char* boja;
    Fakultet fak;
    strcpy(fak.adresa, "Adesa");

    fak.info();

    Pravougaonik p1(3, 3);
    cout << p1.obim() << endl;
    cout << p1.povrsina() << endl;

    //Pravougaonik p(p1);

    Helikopter h;
    h.setBrojSedista(2);

    cout << h.getBrojSedista() << endl;

    return 0;
}

