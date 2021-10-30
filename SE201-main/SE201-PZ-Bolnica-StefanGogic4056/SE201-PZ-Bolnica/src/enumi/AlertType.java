package enumi;

import entiteti.Pacijent;
import entiteti.ZakazanaPoseta;
import java.util.*;
import javafx.scene.control.TextField;

public enum AlertType {
    success,
    error;

    public class ZakazivanjeGUI {

        private TextField jmbgPosetioca;
        private TextField jmbgPacijenta;
        private Date datumPosete;

        public ZakazanaPoseta prikazZakazanePosete;

        public void otvoriZakazivanjeGUI() {
        }

        public void prikazPoruke(String poruka, AlertType tipPoruke) {
            System.out.println(poruka);
        }

        public void sacuvajZakazazanuPosetu(ZakazanaPoseta zakazanaPoseta) {
        }

    }

    public class OtkazivanjePoseteGUI {

        public List<ZakazanaPoseta> prikazZakazanihPoseta;

        public boolean obrisiPosetu;

        public void otvoriOtkazivanjePoseteGUI() {
        }

        public void prikazPoruke(String poruka, AlertType tipPoruke) {
            System.out.println(poruka);
        }

    }

    public class AdministracijaPacijentaGUI {

        private TextField jmbgPacijenta;
        private TextField imePacijenta;
        private TextField prezimePacijenta;
        private TextField stepenBolesti;

        public void prikazPoruke(String poruka, AlertType tipPoruke) {
        }

        public void otvoriAdministracijuPacijentaGUI() {
        }

        public void sacuvajIzmenu(Pacijent pacijent) {
        }

    }

}
