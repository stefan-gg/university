import { Component, Input, OnInit } from '@angular/core';
import { Store } from '@ngrx/store';
import { AppState } from '../app.state';
import { Smestaj } from '../models/smestaj.model';

@Component({
  selector: 'app-single-smestaj',
  templateUrl: './single-smestaj.component.html',
  styleUrls: ['./single-smestaj.component.css']
})
export class SingleSmestajComponent implements OnInit {
  //imeHotela: string;
  //brojSoba: number;
  //opisHotela: string;
  smestaji: Smestaj[]
  smestaj: Smestaj

  constructor(private store: Store<AppState>) {
    let url = window.location.href;
    let brojSobe = parseInt(url.slice(url.lastIndexOf('/') + 1));
    //let json = localStorage.getItem("smestaji");
    //let podaci = JSON.parse(json + "");

    this.store.select("smestaji").subscribe(smestaji => this.smestaji = [...smestaji])
    this.smestaj = this.smestaji[brojSobe];

    //this.imeHotela = podaci[brojSobe].imeHotela;
    //this.brojSoba = podaci[brojSobe].brojSoba;
    //this.opisHotela = podaci[brojSobe].opisHotela;
  }

  ngOnInit(): void {
  }

}
