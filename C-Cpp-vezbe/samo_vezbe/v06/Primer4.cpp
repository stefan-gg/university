#include <iostream>

using namespace std;

int main() {

	/*int brProdavaca, brProdaja;

	cout << "Najeb" ;
	cin >> brProdavaca;

	cout << "Najeb";
	cin >> brProdaja;

	for (int i = 0; i < brProdavaca; i++) {
		float vrProdaje, ukupna = 0;
		float prosek;
		for (int j = 0; j < brProdaja; j++) {
			cout << "Unesite vrednost prodaje" << j << " za prodavca" << i << ":";
			cin >> vrProdaje;
			ukupna += vrProdaje;
		}
		cout << endl;
		prosek = ukupna / brProdaja;
		cout << "Prosek" << i << " je " << prosek << endl;
	}*/

	double root2 = sqrt(2);
	int places;

	for (places = 0; places < 10; places++)
	{
		cout.precision(places);
		cout << root2 << endl;
		//cout << setprecison(places) << root2 << endl;
	}

	return 0;
}