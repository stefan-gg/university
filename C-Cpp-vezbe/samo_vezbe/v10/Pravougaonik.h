#pragma once
#include "Oblik.h"
class Pravougaonik : public Oblik
{
public:
	int povrsina() {
		return sirina * visina;
	}

};

