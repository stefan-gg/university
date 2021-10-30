package entiteti;

import abstraktneKlase.Dekorator;

public class PorodicnaPosetaDekorator extends Dekorator {

    @Override
    public void vrstaPosete(ZakazanaPoseta zakazanaPoseta) {
        zakazanaPoseta.setVrstaPosete("U posetu će doći samo uža porodica.");
    }

}
