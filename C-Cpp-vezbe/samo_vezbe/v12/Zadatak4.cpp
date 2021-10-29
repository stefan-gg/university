#include <iostream>
using namespace std;
#include <vector>
#include <iterator>
#include <algorithm>

bool veciOd10(int v) {
	return v > 10;
}

int main() {

	const int SIZE = 6;
	int niz[6] = {1, 2, 3, 4, 5, 6};
	vector<int> intVector(niz, niz + SIZE);

	ostream_iterator<int> output(cout, " ");
	cout << "Vektor sadrzi : " << endl;
	copy(intVector.begin(), intVector.end(), output);
	cout << endl;

	vector<int>::iterator location;
	location = find(intVector.begin(), intVector.end(), 10);

	if (location != intVector.end()) {
		cout << "" << distance(intVector.begin(), location) << endl;
	}
	else {
		cout << "Nije pronadjen broj 10" << endl;
	}

	location = find_if(intVector.begin(), intVector.end(), veciOd10);

	if (location != intVector.end()) {
		cout << "Element : " << *location << endl;
	}
	else {
		cout << "Nije pronadjen broj 10" << endl;
	}


	sort(intVector.begin(), intVector.end());
    copy(intVector.begin(), intVector.end(), output);
	cout << endl;

	if (binary_search(intVector.begin(), intVector.end(), 4)) {
		cout << "ima 4" << endl;
	}
	else {
		cout << "nema 4" << endl;
	}



	/*
	cout << "Vektor sadrzi : " << endl;
	copy(intVector.begin(), intVector.end(), output);
	
	intVector[0] = 7;//sporije je
	intVector.at(2) = 10;
	
	intVector.insert(intVector.begin() + 1, 22);
	
	//intVector.erase(intVector.begin(), intVector.end());

	intVector.erase(intVector.begin());
	*/



	return 0;
}