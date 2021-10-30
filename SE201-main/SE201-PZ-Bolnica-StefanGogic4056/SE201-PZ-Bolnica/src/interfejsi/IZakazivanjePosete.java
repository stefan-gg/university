package interfejsi;

import entiteti.Pacijent;
import entiteti.ZakazanaPoseta;
import java.util.*;

public interface IZakazivanjePosete {

    void pregledZakazanePosete(ZakazanaPoseta zakazanaPoseta);

    boolean mogucnostZakazivanjaPosete(String jmbgPacijenta, String jmbgPosetioca, Date datumPosete);

    boolean proveraValidnostiJMBG(String jmbgPacijenta);

    boolean proveraStepenaBolesti(Pacijent pacijent);

    List<ZakazanaPoseta> zakazanePosete(String jmbgPosetioca);

}
