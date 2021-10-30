
package entiteti;

import abstraktneKlase.Dekorator;

public class PojedinacnaPosetaDekorator extends Dekorator {

    @Override
    public void vrstaPosete(ZakazanaPoseta zakazanaPoseta) {
        zakazanaPoseta.setVrstaPosete("U posetu će doći samo jedna osoba.");
    }
    
}
