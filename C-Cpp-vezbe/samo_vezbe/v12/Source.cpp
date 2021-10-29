#include <iostream>
using namespace std;
#include <vector>
#include <iterator>

template <typename T>
void printVector(const vector<T>& v) {
	typename vector<T>::const_iterator constIt;
	for (constIt = v.begin(); constIt != v.end(); constIt++) {
		cout << *constIt << "" << endl;
	}
}

int main() {
	//zad 3
	//uvecava kapacitet 1.5 puta
	const int SIZE = 6;
	vector<int> iVec;

	iVec.push_back(1);
	iVec.push_back(2);
	iVec.push_back(3);

	cout << "Velicina vektora->" << iVec.size() << ",kapacitet ->" << iVec.capacity() << endl;

	printVector(iVec);

	vector<int>::const_reverse_iterator revIt;

	for (revIt = iVec.rbegin(); revIt != iVec.rend(); revIt++) {
		cout << *revIt << endl;
	}


	return 0;
}