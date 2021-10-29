#pragma once
#include <iostream>
#include <string>
using namespace std;

class Student {
public :
	string ime;
	int brIndeksa;

	Student();
	Student(string ime, int brIndeksa);
	Student(const Student& s);
	~Student();
private :
};
