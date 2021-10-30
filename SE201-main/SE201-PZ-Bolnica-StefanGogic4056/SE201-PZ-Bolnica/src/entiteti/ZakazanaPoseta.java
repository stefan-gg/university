package entiteti;

import interfejsi.IZakazivanjePosete;
import interfejsi.IOtkazivanjePosete;
import izuzeci.JMBGException;
import java.util.*;

public class ZakazanaPoseta implements IZakazivanjePosete, IOtkazivanjePosete {

    private String jmbgPacijenta;
    private String jmbgPosetioca;
    private Date datumPosete;
    private boolean otkazanaPoseta;
    private String vrstaPosete;

    public ZakazanaPoseta() {
    }

    public ZakazanaPoseta(String jmbgPacijenta, String jmbgPosetioca, Date datumPosete) {
        this.jmbgPacijenta = jmbgPacijenta;
        this.jmbgPosetioca = jmbgPosetioca;
        this.datumPosete = datumPosete;
    }

    public String getJmbgPacijenta() {
        return jmbgPacijenta;
    }

    public void setJmbgPacijenta(String newJmbgPacijenta) throws JMBGException {
        if (newJmbgPacijenta.length() == 13) {
            jmbgPacijenta = newJmbgPacijenta;
        } else {
            throw new JMBGException("JMBG mora da ima dužinu od 13 broja !!!");
        }
    }

    public String getJmbgPosetioca() {
        return jmbgPosetioca;
    }

    public void setJmbgPosetioca(String newJmbgPosetioca) throws JMBGException {
        if (newJmbgPosetioca.length() == 13) {
            jmbgPosetioca = newJmbgPosetioca;
        } else {
            throw new JMBGException("JMBG mora da ima dužinu od 13 broja !!!");
        }
    }

    public Date getDatumPosete() {
        return datumPosete;
    }

    public void setDatumPosete(Date newDatumPosete) {
        datumPosete = newDatumPosete;
    }

    public boolean isOtkazanaPoseta() {
        return otkazanaPoseta;
    }

    public void setOtkazanaPoseta(boolean otkazanaPoseta) {
        this.otkazanaPoseta = otkazanaPoseta;
    }

    public String getVrstaPosete() {
        return vrstaPosete;
    }

    public void setVrstaPosete(String vrstaPosete) {
        this.vrstaPosete = vrstaPosete;
    }

    @Override
    public boolean mogucnostZakazivanjaPosete(String jmbgPacijenta, String jmbgPosetioca, Date datumPosete) {
        //Lista sa svim pacijentima iz koje se pronalazi pacijent sa unetim JMBG-om i proverava se njegov stepen bolesti
        List<Pacijent> pacijenti = new ArrayList<>();
        Pacijent p = new Pacijent("1231231231231", "1231231231231", 3, 5, "1231231231231");

        pacijenti.add(p);

        boolean validanJmbg = proveraValidnostiJMBG(jmbgPacijenta);
        if (validanJmbg == true) {
            for (Pacijent pacijent : pacijenti) {
                if (pacijent.getJmbg().equals(jmbgPacijenta)) {
                    if (pacijent.getStepenBolesti() > 3) {
                        return false;
                    }
                    return true;
                }
            }
        }
        return false;
    }

    @Override
    public boolean proveraValidnostiJMBG(String jmbgPacijenta) {
        //proverava se validnost odnosno dali postoji pacijent sa unetim JMBG-om
        boolean validanJMBG = false;
        if (jmbgPacijenta.length() != 13) {
            return validanJMBG;
        }
        List<Pacijent> pacijenti = new ArrayList<>();
        for (Pacijent pacijent : pacijenti) {
            if (pacijent.getJmbg().equals(jmbgPacijenta)) {
                validanJMBG = true;
            }
        }
        return validanJMBG;
    }

    @Override
    public boolean otkazanaPoseta(String jmbgPacijenta, String jmbgPosetioca, Date datumPosete) {
        return true;
    }

    @Override
    public List<ZakazanaPoseta> zakazanePosete(String jmbgPosetioca) {
        //lista sa svim zakazanim posetama koje se citaju iz baze
        List<ZakazanaPoseta> zakazanePosete = new ArrayList<>();
        //Lista koja ce da sadrzi sve zakazane posete odredjenog posetioca
        List<ZakazanaPoseta> zakazanePosetePosetoica = new ArrayList<>();
        //provera koja zakazana poseta ima jmbg isti kao i jmbg posetioca
        for (ZakazanaPoseta zakazanaPoseta : zakazanePosete) {
            if (zakazanaPoseta.getJmbgPosetioca().equals(jmbgPosetioca)) {
                zakazanePosetePosetoica.add(zakazanaPoseta);
            }
        }

        return zakazanePosetePosetoica;
    }

    @Override
    public List<ZakazanaPoseta> prikazZakazanihPoseta(String jmbg) {
        //lista sa svim zakazanim posetama koje se citaju iz baze
        List<ZakazanaPoseta> sveZakazanePosete = new ArrayList<>();
        //Lista koja ce da sadrzi sve zakazane posete za odredjeni jmbg
        List<ZakazanaPoseta> zakazanePosete = new ArrayList<>();
        //provera koja zakazana poseta ima jmbg isti kao i jmbg posetioca ili jmbg pacijenta
        for (ZakazanaPoseta zakazanaPoseta : sveZakazanePosete) {
            if (zakazanaPoseta.getJmbgPacijenta().equals(jmbg) || zakazanaPoseta.getJmbgPosetioca().equals(jmbg)) {
                zakazanePosete.add(zakazanaPoseta);
            }
        }

        return zakazanePosete;
    }

    @Override
    public void pregledZakazanePosete(ZakazanaPoseta zakazanaPoseta) {
        System.out.println("JMBG posetica" + zakazanaPoseta.getJmbgPosetioca()
                + "\n" + "JMBG pacijenta" + zakazanaPoseta.getJmbgPacijenta()
                + "\n" + "Datum posete" + zakazanaPoseta.getDatumPosete());
    }

    @Override
    public boolean potvrdaOtkazivanjaPosete(String odgovor) {
        if (odgovor.equals("da") || odgovor.equals("Da")) {
            return true;
        }
        return false;
    }

    @Override
    public boolean proveraStepenaBolesti(Pacijent pacijent) {
        if (pacijent.getStepenBolesti() > 3) {
            return false;
        }
        return true;
    }

}
