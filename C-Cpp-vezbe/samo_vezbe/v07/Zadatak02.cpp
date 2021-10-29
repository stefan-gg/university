#include <iostream>
using namespace std;

void useLocal();
void useGlobal();

int x = 1;//globalna

int main()
{
	cout << x << endl;

	int x = 2;

	cout << x << endl;

	if (true) {
		int x = 3;
		cout << x << endl;
	}

	useLocal();
	useGlobal();//stampa x iz main
	cout << x << endl;//x je  2 jer samo u f-ju vazi vrednost

	return 0;
}

void useLocal() {
	/*int x = 25;
	cout << "aa " << x << " bb" <<endl;
	x++;
	cout << "aa " << x << " bb" << endl;*/
	static int x = 25;//kad se pozove x ima
	//vrednost koju je imao na izlazu(26)
	cout << "aa " << x << " bb" << endl;
	x++;
	cout << "aa " << x << " bb" << endl;
}

void useGlobal() {
	cout << "aa " << x << " globalno" << endl;
}