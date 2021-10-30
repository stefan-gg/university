package entiteti;

import abstraktneKlase.Osoba;
import izuzeci.BrojTelefonaException;
import izuzeci.JMBGException;

public class Posetilac extends Osoba {

    private String brojTelefona;
    private String jmbg;

    public java.util.List<ZakazanaPoseta> zakazanaPoseta;

    public String getBrojTelefona() {
        return brojTelefona;
    }

    public void setBrojTelefona(String newBrojTelefona) throws BrojTelefonaException {
        if (newBrojTelefona.substring(0, 2).equals("06") && newBrojTelefona.length() >= 4) {
            brojTelefona = newBrojTelefona;
        } else {
            throw new BrojTelefonaException("Broj telefona koji ste uneli nije u ispravnom formatu");
        }

    }

    public String getJmbg() {
        return jmbg;
    }

    public void setJmbg(String newJmbg) throws JMBGException {
        if (newJmbg.length() == 13) {
            jmbg = newJmbg;
        } else {
            throw new JMBGException("JMBG mora da ima dužinu od 13 broja !!!");
        }
    }

    public Posetilac() {

    }

    public Posetilac(String brojTelefona, String jmbg, String ime, String prezime) {
        super(ime, prezime);
        this.ime = ime;
        this.prezime = prezime;
        this.jmbg = jmbg;
        this.brojTelefona = brojTelefona;

    }

    public java.util.List<ZakazanaPoseta> getZakazanaPoseta() {
        if (zakazanaPoseta == null) {
            zakazanaPoseta = new java.util.ArrayList<>();
        }
        return zakazanaPoseta;
    }

    public java.util.Iterator getIteratorZakazanaPoseta() {
        if (zakazanaPoseta == null) {
            zakazanaPoseta = new java.util.ArrayList<>();
        }
        return zakazanaPoseta.iterator();
    }

    public void setZakazanaPoseta(java.util.List<ZakazanaPoseta> newZakazanaPoseta) {
        removeAllZakazanaPoseta();
        for (java.util.Iterator iter = newZakazanaPoseta.iterator(); iter.hasNext();) {
            addZakazanaPoseta((ZakazanaPoseta) iter.next());
        }
    }

    public void addZakazanaPoseta(ZakazanaPoseta newZakazanaPoseta) {
        if (newZakazanaPoseta == null) {
            return;
        }
        if (this.zakazanaPoseta == null) {
            this.zakazanaPoseta = new java.util.ArrayList<>();
        }
        if (!this.zakazanaPoseta.contains(newZakazanaPoseta)) {
            this.zakazanaPoseta.add(newZakazanaPoseta);
        }
    }

    public void removeZakazanaPoseta(ZakazanaPoseta oldZakazanaPoseta) {
        if (oldZakazanaPoseta == null) {
            return;
        }
        if (this.zakazanaPoseta != null) {
            if (this.zakazanaPoseta.contains(oldZakazanaPoseta)) {
                this.zakazanaPoseta.remove(oldZakazanaPoseta);
            }
        }
    }

    public void removeAllZakazanaPoseta() {
        if (zakazanaPoseta != null) {
            zakazanaPoseta.clear();
        }
    }

}
