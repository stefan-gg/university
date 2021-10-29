#include <iostream>
using namespace std;
#include <vector>
#include <iterator>
//#include <algorithm>
#include <list>
#include <stack>

template <typename T>
void pushElements(T& stack) {
	for (int i = 0; i < 10; i++) {
		stack.push(i);
	}
}

template <typename T>
void popElement(T& stack) {
	while (!stack.empty()) {
		cout << stack.top() << " ";
		stack.pop();
	}
}

int main() {

	stack<int> intDequeStack;
	stack<int, vector<int>> intVectorStack;
	stack<int, list<int>> intListStack;

	pushElements(intDequeStack);
	pushElements(intVectorStack);
	pushElements(intListStack);

	return 0;
}