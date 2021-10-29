#pragma once
#include <iostream>
using namespace std;

const int SIZE = 100;

template<class T>
class Stack
{
private:
	T st[SIZE];
	int top;

public:
	Stack() {
		top = -1;
	}
	void push(T el);
	T pop();

};

template <class T>
void Stack<T>::push(T el) {
	if (top == SIZE) {
		cout << "Stack is full" << endl;
	}
	st[++top] = el;
}

template <class T>
T Stack<T>::pop() {
	if (top == -1) {
		cout << "Prazan" << endl;
		return;
	}
	return st[top--];
}

