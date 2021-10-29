#include <iostream>
using namespace std;
#include <vector>
#include <iterator>
#include <algorithm>
#include <list>
#include <stack>
#include<cstdlib>

int main() {
	/*
	Zadatak 01.
	vector<int> vec;
	int i;

	cout << "Velicina" << vec.size() << endl;
	

	for (i = 0; i < 5; i++) {
		vec.push_back(i);
	}

	cout << "napred : " << vec.front() << endl;
	cout << "nazad : " << vec.back() << endl;
	cout << "Da li je prazan ?" << vec.empty() << endl;

	for (i = 0; i < vec.size(); i++) {
		cout << "vrednost " << endl;
	}

	vector<int>::iterator it = vec.begin();

	while (it != vec.end()) {
		cout << "vrednost iteratora je" << *it << endl;
		it++;

		*****************************************************
	}*/

	/*cout << "Unesite dva broja :" << endl;
	istream_iterator<int> inputIt(cin);
	int broj1 = *inputIt;
	inputIt++;
	int broj2 = *inputIt;

	ostream_iterator<int> outputIt(cout);
	cout << "Zbir je : ";
	*outputIt = broj1 + broj2;*/

	int max = 500;
	
	//stack<float> intDequeStack;

	vector<float> vec;
	vector<float>::iterator it = vec.begin();

	while(it != vec.end()) {
		srand(time(0));
		float br = (rand() % max) / 100;
		*it = br;
		it++;
	}

	while (it != vec.end()) {
		if (it == vec.begin()) {
			*it = 10;
		}
		if (it == vec.end() - 1) {
			*it = 25;
		}
		if (it == vec.end() - 3) {
			*it *= 6.0;
		}
		
		it++;
	}


	//max = 500;
	//srand(time(0));
	//float br2 = (rand() % max) / 100;

	//intDequeStack.pop();
	//intDequeStack.push(25);


	return 0;
}
