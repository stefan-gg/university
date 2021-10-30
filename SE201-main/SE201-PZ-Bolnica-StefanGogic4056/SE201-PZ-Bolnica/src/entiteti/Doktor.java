package entiteti;

import abstraktneKlase.Osoba;

public class Doktor extends Osoba {

    private int idBroj;
    private String specijalizacija;

    public java.util.List<ZakazanaPoseta> zakazanaPoseta;
    public java.util.List<Pacijent> pacijent;
    public java.util.List<Osoba> osobe;

    public int getIdBroj() {
        return idBroj;
    }

    public void setIdBroj(int newIdBroj) {
        idBroj = newIdBroj;
    }

    public String getSpecijalizacija() {
        return specijalizacija;
    }

    public void setSpecijalizacija(String newSpecijalizacija) {
        specijalizacija = newSpecijalizacija;
    }

    public Doktor() {
    }

    public Doktor(String ime, String prezime, int idBroj, String specijalizacija) {
        super(ime, prezime);
        this.ime = ime;
        this.prezime = prezime;
        this.idBroj = idBroj;
        this.specijalizacija = specijalizacija;
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

    public java.util.List<Pacijent> getPacijent() {
        if (pacijent == null) {
            pacijent = new java.util.ArrayList<>();
        }
        return pacijent;
    }

    public java.util.Iterator getIteratorPacijent() {
        if (pacijent == null) {
            pacijent = new java.util.ArrayList<>();
        }
        return pacijent.iterator();
    }

    public void setPacijent(java.util.List<Pacijent> newPacijent) {
        removeAllPacijent();
        for (java.util.Iterator iter = newPacijent.iterator(); iter.hasNext();) {
            addPacijent((Pacijent) iter.next());
        }
    }

    public void addPacijent(Pacijent newPacijent) {
        if (newPacijent == null) {
            return;
        }
        if (this.pacijent == null) {
            this.pacijent = new java.util.ArrayList<>();
        }
        if (!this.pacijent.contains(newPacijent)) {
            this.pacijent.add(newPacijent);
        }
    }

    public void removePacijent(Pacijent oldPacijent) {
        if (oldPacijent == null) {
            return;
        }
        if (this.pacijent != null) {
            if (this.pacijent.contains(oldPacijent)) {
                this.pacijent.remove(oldPacijent);
            }
        }
    }

    public void removeAllPacijent() {
        if (pacijent != null) {
            pacijent.clear();
        }
    }

    public java.util.List<Osoba> getOsobe() {
        if (osobe == null) {
            osobe = new java.util.ArrayList<>();
        }
        return osobe;
    }

    public java.util.Iterator getIteratorOsobe() {
        if (osobe == null) {
            osobe = new java.util.ArrayList<>();
        }
        return osobe.iterator();
    }

    public void setOsobe(java.util.List<Osoba> newOsobe) {
        removeAllOsobe();
        for (java.util.Iterator iter = newOsobe.iterator(); iter.hasNext();) {
            addOsobe((Osoba) iter.next());
        }
    }

    public void addOsobe(Osoba newOsoba) {
        if (newOsoba == null) {
            return;
        }
        if (this.osobe == null) {
            this.osobe = new java.util.ArrayList<>();
        }
        if (!this.osobe.contains(newOsoba)) {
            this.osobe.add(newOsoba);
        }
    }

    public void removeOsobe(Osoba oldOsoba) {
        if (oldOsoba == null) {
            return;
        }
        if (this.osobe != null) {
            if (this.osobe.contains(oldOsoba)) {
                this.osobe.remove(oldOsoba);
            }
        }
    }

    public void removeAllOsobe() {
        if (osobe != null) {
            osobe.clear();
        }
    }

}
