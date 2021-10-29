#include <iostream>
#include <fstream>

using namespace std;

int main() {

    fstream file("example.txt");
    int number;

    for (int i = 1; i <= 10; i++) {
        cout << i;
        if (i == 10) {
            file << i;
        }
        else {
            file << i << endl;
        }
    }
    file.close();

    file.open("example.txt");
    file >> number;
    while (!file.eof()) {
        cout << number << endl;
        file >> number;
    }

    file.close();

    return 0;
}