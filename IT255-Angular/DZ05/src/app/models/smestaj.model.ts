export class Smestaj {
    
    imeHotela: string;
    opisHotela: string;
    brojSoba: string;
    cenaSobe: number;
    brojRezervisanihDana: number;

    constructor(imeHotela: string, brojSoba: string, opisHotela: string, cenaSobe: number, brojRezervisanihDana: number) {
        this.imeHotela = imeHotela;
        this.brojSoba = brojSoba;
        this.opisHotela = opisHotela;
        this.cenaSobe = cenaSobe;
        this.brojRezervisanihDana = brojRezervisanihDana;
    }
}