#pragma once
class Prodaja
{
	double prodajaPoMesecima[12];
	double ukupnaGodProdaja();
public:
	Prodaja();
	void unesiProdaje();
	void setProdaja(int i, double p);
	void stampanjeProdaje();
	//mora referencu da vraca
	double& operator[](int i);
};

