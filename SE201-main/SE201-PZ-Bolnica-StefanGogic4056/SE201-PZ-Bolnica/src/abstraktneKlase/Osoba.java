package abstraktneKlase;

public abstract class Osoba {

    public String ime;
    public String prezime;

    public String getIme() {
        return ime;
    }

    public void setIme(String newIme) {
        ime = newIme;
    }

    public String getPrezime() {
        return prezime;
    }

    public void setPrezime(String newPrezime) {
        prezime = newPrezime;
    }

    public Osoba() {
    }

    public Osoba(String ime, String prezime) {
        this.ime = ime;
        this.prezime = prezime; 
    }

}
