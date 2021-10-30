package interfejsi;

import entiteti.Pacijent;
import java.util.*;

public interface IAdministracijaPacijenta {

    void obrisiPacijenta(String jmbgPacijenta);

    void pogledajPodatkeOPacijentu(String jmbgPacijenta);

    void dodajPacijenta(Pacijent pacijent);

    void azurirajPacijenta(Pacijent pacijent);

    List<Pacijent> prikazSvihPacijenata(int idBroj);

}
