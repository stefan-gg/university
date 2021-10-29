#include "Kompleksni.h"

ostream& operator<<(ostream& out, const Kompleksni a)
{
    out << a.real << " + " << a.imag << "i" << endl;
    return out;
}

bool Kompleksni::operator>(const Kompleksni& k) {
    if (this->real > k.real) {
        return true;
    }
    else if (this->real == k.real) {
        if (this->imag > k.imag)
            return true;
    }
    return false;
}

/*bool operator<(const Kompleksni& a, const Kompleksni& b)
{
    if (a.real < b.real && a.imag < b.imag)
    {
        return true;
    }
    else if (a.real == b.real) {
        if (a.imag > b.imag) {
            return true;
        }
        else {
            return false;
        }
        
    }
    else{
        return false;
    }

    
    
}*/