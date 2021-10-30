package interfejsi;

import entiteti.ZakazanaPoseta;
import java.util.*;

public interface IBrisanjePosete {

    boolean obrisanaPoseta(String jmbgPacijenta, String jmbgPosetioca, Date datumPosete);

    List<ZakazanaPoseta> prikazZakazanihPoseta(String jmbg);

    boolean potvrdaBrisanjaPosete(String odgovor);

}
