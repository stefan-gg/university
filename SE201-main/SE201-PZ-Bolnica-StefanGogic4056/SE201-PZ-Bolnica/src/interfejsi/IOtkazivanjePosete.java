package interfejsi;

import entiteti.ZakazanaPoseta;
import java.util.*;

public interface IOtkazivanjePosete {

    boolean otkazanaPoseta(String jmbgPacijenta, String jmbgPosetioca, Date datumPosete);

    List<ZakazanaPoseta> prikazZakazanihPoseta(String jmbg);

    boolean potvrdaOtkazivanjaPosete(String odgovor);

}
