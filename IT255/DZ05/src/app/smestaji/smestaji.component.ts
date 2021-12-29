import { Component, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { AppState } from '../app.state';
import { Smestaj } from '../models/smestaj.model';
import * as SmestajActions from '../actions/smestaj.actions';

@Component({
  selector: 'app-smestaji',
  templateUrl: './smestaji.component.html',
  styleUrls: ['./smestaji.component.css']
})
export class SmestajiComponent implements OnInit {
  //public lista_svih_smestaja: Smestaj[] = [];
  smestaji: Smestaj[]
  ngOnInit(): void {
  }

  

  constructor(private store: Store<AppState>) {
    //this.lista_svih_smestaja = [new Smestaj("Ime hotela", "21", "Opis hotela, opis hotela.", 23, 3),
    //new Smestaj("Ime drugog hotela", "291", "Hotel se nalazi u sred pustinje.", 2, 2)];
    this.store.select("smestaji").subscribe(smestaji => this.smestaji = [...smestaji]);
  }

  addSmestaj(smestaj: Smestaj): void {
    this.store.dispatch(new SmestajActions.DodajSobu(smestaj));
    //this.lista_svih_smestaja.push(smestaj);
    //console.log(this.lista_svih_smestaja);
    //localStorage.setItem("smestaji", JSON.stringify(this.lista_svih_smestaja));
  }

  deleteIzabraniSmestaj(smestaj: Smestaj) {
   this.store.dispatch(new SmestajActions.ObrisiSobu(smestaj)) 
   //var lista = this.lista_svih_smestaja;
   //var novaLista = [];
   //for (const element of lista) {
   //  if (element !== smestaj) {
   //    novaLista.push(element);
   //  }
   //}
   //this.lista_svih_smestaja = novaLista;
   //localStorage.setItem("smestaji", JSON.stringify(this.lista_svih_smestaja));
  }

  shuffleSmestaj() {
    let velicinaNiza = this.smestaji.length;

    while (0 !== velicinaNiza) {
      let randomIndex = Math.floor(Math.random() * velicinaNiza);
      velicinaNiza--;
      //dolazi do zamene vrednosti izmedju 2 promenljive
      let privremeni = this.smestaji[velicinaNiza];
      this.smestaji[velicinaNiza] = this.smestaji[randomIndex];
      this.smestaji[randomIndex] = privremeni;
    }

    return this.smestaji;
  }
}
