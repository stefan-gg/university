import { Component } from '@angular/core';
import { Smestaj } from './models/smestaj.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'DZ05-MetHotels';
  public lista_svih_smestaja: Smestaj[] = [];

  constructor() {
    this.lista_svih_smestaja = [new Smestaj("Ime hotela", "21", "Opis hotela, opis hotela.", 23, 3),
    new Smestaj("Ime drugog hotela", "291", "Hotel se nalazi u sred pustinje.", 2, 2)];
  }

  addSmestaj(smestaj: Smestaj): void {
    this.lista_svih_smestaja.push(smestaj);
    console.log(this.lista_svih_smestaja);
  }

  deleteIzabraniSmestaj(smestaj: Smestaj) {
    var lista = this.lista_svih_smestaja;
    var novaLista = [];
    for (const element of lista) {
      if (element !== smestaj) {
        novaLista.push(element);
      }
    }
    this.lista_svih_smestaja = novaLista;
  }

  shuffleSmestaj() {
    let velicinaNiza = this.lista_svih_smestaja.length;

    while (0 !== velicinaNiza) {
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

