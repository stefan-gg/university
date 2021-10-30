package entiteti;

import interfejsi.IAdministracijaPacijenta;
import abstraktneKlase.Osoba;
import izuzeci.JMBGException;
import java.util.*;

public class Pacijent extends Osoba implements IAdministracijaPacijenta {

    private int stepenBolesti;
    private int idBrojIzabranogDoktora;
    private String jmbg;
    private boolean otpustenIzBolnice;

    public java.util.List<ZakazanaPoseta> zakazanaPoseta;

    public int getStepenBolesti() {
        return stepenBolesti;
    }

    public void setStepenBolesti(int newStepenBolesti) {
        stepenBolesti = newStepenBolesti;
    }

    public int getIdBrojIzabranogDoktora() {
        return idBrojIzabranogDoktora;
    }

    public void setIdBrojIzabranogDoktora(int newIdBrojIzabranogDoktora) {
        idBrojIzabranogDoktora = newIdBrojIzabranogDoktora;
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

    public boolean isOtpustenIzBolnice() {
        return otpustenIzBolnice;
    }

    public void setOtpustenIzBolnice(boolean otpustenIzBolnice) {
        this.otpustenIzBolnice = otpustenIzBolnice;
    }

    public Pacijent() {
    }

    public Pacijent(String ime, String prezime, int stepenBolesti, int idIzabranogDoktora, String jmbg) {
        super(ime, prezime);
        this.ime = ime;
        this.prezime = prezime;
        this.stepenBolesti = stepenBolesti;
        this.idBrojIzabranogDoktora = idIzabranogDoktora;
        this.jmbg = jmbg;
    }

    @Override
    public void otpustiPacijenta(String jmbgPacijenta) {
        // brisanje pacijenta sa datim JMBG-om iz baze ako postoji
        List<Pacijent> pacijenti = new ArrayList<>();
        for (Pacijent pacijent : pacijenti) {
            if (pacijent.getJmbg().equals(jmbgPacijenta)) {
                pacijenti.remove(pacijent);
            }
        }
    }

    @Override
    public void pogledajPodatkeOPacijentu(String jmbgPacijenta) {
        //prikaz liste svih pacijenata i trazenje onog sa datim JMBG-om
        List<Pacijent> pacijenti = new ArrayList<>();
        for (Pacijent pacijent : pacijenti) {
            if (pacijent.getJmbg().equals(jmbgPacijenta)) {
                System.out.println(pacijent.toString());
            }
        }
    }

    @Override
    public void dodajPacijenta(Pacijent pacijent) {
        List<Pacijent> pacijenti = new ArrayList<>();
        pacijenti.add(pacijent);
    }

    @Override
    public void azurirajPacijenta(Pacijent pacijent) {
        //na osnovu podataka ce se ili sacuvati novi pacijent ili ce se azurirati postojeci
        List<Pacijent> pacijenti = new ArrayList<>();
        for (Pacijent pacijentt : pacijenti) {
            if (pacijentt.getJmbg().equals(pacijent.getJmbg())) {
                pacijentt.setIme(pacijent.getIme());
                pacijentt.setPrezime(pacijent.getPrezime());
                pacijentt.setIdBrojIzabranogDoktora(pacijent.getIdBrojIzabranogDoktora());
                pacijentt.setStepenBolesti(pacijent.getStepenBolesti());
                pacijentt.setStepenBolesti(pacijent.getStepenBolesti());
            }
        }
    }

    @Override
    public List<Pacijent> prikazSvihPacijenata(int idBroj) {
        //iz liste svih pacijenata se traže oni koji imaju isti idBroj kao i uneti idBroj
        List<Pacijent> pacijenti = new ArrayList<>();
        List<Pacijent> pacijentiDoktora = new ArrayList<>();

        for (Pacijent pacijent : pacijenti) {
            if (pacijent.getIdBrojIzabranogDoktora() == idBroj) {
                pacijentiDoktora.add(pacijent);
            }
        }
        return pacijentiDoktora;
    }

    public java.util.List<ZakazanaPoseta> getZakazanaPoseta() {
        if (zakazanaPoseta == null) {
            zakazanaPoseta = new java.util.ArrayList<ZakazanaPoseta>();
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

    @Override
    public String toString() {
        return "Pacijent{" + "stepenBolesti=" + stepenBolesti + ", idBrojIzabranogDoktora=" + idBrojIzabranogDoktora + ", jmbg=" + jmbg + ", zakazanaPoseta=" + zakazanaPoseta + '}';
    }

}
