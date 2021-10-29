#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {

	string s;
	cout << "Unesite nesto \n";
	getline(cin, s);
	cout << s;*///unos reci za razmakom

	char c, ans;
	ans = 'y';
	cout << "asd";
	ofstream out("tekst.txt");
	if (out.is_open()) {
		while (ans == 'y')
		{
			cout << endl << "Unesite karakter";
			cin >> c;
			out.put(c);

			cout << "Da li nastavljate sa unosom ?";
			cin >> ans;
		}
	}
	out.close();
	cout << "asd2";
	ifstream in("tekst.txt");
	if (in.is_open()) {
		while (!in.eof()) {
			c = in.get();

			if (!in.eof()) {
				cout << c;
			}
		}
	}
	in.close();
	cout << "as3";
	return 0;

	int i = 1;
	int c = 1;
	ofstream out("tekst.txt");
	if (out.is_open()) {
		while (i < 11)
		{
			out.put(i);
			i++;
		}
	}

	out.close();

	ifstream in("tekst.txt");
	if (in.is_open()) {
		while (!in.eof()) {
			c = in.get();

			if (!in.eof()) {
				cout << c;
			}
		}
	}
	in.close();
	return 0;*
}
		/*
}
/*#include <iostream>
#include <fstream>

using namespace std;

int main() {

	fstream file("example.txt");
	int number;

	for (int i = 1; i <= 10; i++) {
		if (i == 10) {
			file << i;
		}
		else {
			file << i << endl;
		}
	}
	file.close();

	file.open("example.txt");
	while (!file.eof()) {
		file >> number;
		cout << number << endl;
	}

	file.close();

	return 0;
}*/