#include "Student.h"
#include <iostream>
using namespace std;

Student::Student(){
	ime = "Student X";
    brIndeksa = 3000;
}

Student::Student(string ime, int brIndeksa) : ime(ime), brIndeksa(brIndeksa){}

Student::Student(const Student& student) {
	this->ime = student.ime;
	this->brIndeksa = student.brIndeksa;
}
/*Student::Student(const Student& s) {
	string* imee = &ime;
	strcpy(ime, *imee);
	brIndeksa = s.brIndeksa;
}*/