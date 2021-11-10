import { Component } from '@angular/core';
import { Smestaj } from './smestaj/smestaj.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'DZ05-MetHotels';
  lista_svih_smestaja: Smestaj[];

  constructor() {
    this.lista_svih_smestaja = [new Smestaj("Ime hotela", "21", "Opis hotela, opis hotela."),
    new Smestaj("Ime drugog hotela", "291", "Hotel se nalazi u sred pustinje.")];
  }

  addSmestaj(imeHotela: HTMLInputElement, brojSoba: HTMLInputElement, opisHotela: HTMLTextAreaElement): boolean {
    console.log(imeHotela.value);
    console.log(brojSoba.value)

    this.lista_svih_smestaja.push(new Smestaj(imeHotela.value, brojSoba.value, opisHotela.value));

    console.log(this.lista_svih_smestaja);

    imeHotela.value = "";
    brojSoba.value = "";
    opisHotela.value = "";

    return false;
  }

  shuffleSmestaj() {
    let velicinaNiza = this.lista_svih_smestaja.length

    while(0 !== velicinaNiza){
      let randomIndex = Math.floor(Math.random() * velicinaNiza);
      velicinaNiza--;
      //dolazi do zamene vrednosti izmedju 2 promenljive
      let privremeni = this.lista_svih_smestaja[velicinaNiza];
      this.lista_svih_smestaja[velicinaNiza] = this.lista_svih_smestaja[randomIndex];
      this.lista_svih_smestaja[randomIndex] = privremeni;
    }
    
    return this.lista_svih_smestaja;
  }

}

