#pragma once
#include "Osnovna.h"
class Izvedena : public Osnovna
{
	int getPodatak() {
		return Osnovna::getPodatak();
	}
	void prikazi() {}
};

