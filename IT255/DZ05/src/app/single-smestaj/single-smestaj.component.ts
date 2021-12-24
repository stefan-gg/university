import { JsonPipe } from '@angular/common';
import { Component, Input, OnInit } from '@angular/core';
import { Smestaj } from '../smestaj/smestaj.model';

@Component({
  selector: 'app-single-smestaj',
  templateUrl: './single-smestaj.component.html',
  styleUrls: ['./single-smestaj.component.css']
})
export class SingleSmestajComponent implements OnInit {
  imeHotela: string;
  brojSoba: number;
  opisHotela: string;

  constructor() {
    let url = window.location.href;
    let brojSobe = parseInt(url.slice(url.lastIndexOf('/') + 1));
    let json = localStorage.getItem("smestaji");
    let podaci = JSON.parse(json + "");

    this.imeHotela = podaci[brojSobe].imeHotela;
    this.brojSoba = podaci[brojSobe].brojSoba;
    this.opisHotela = podaci[brojSobe].opisHotela;
  }

  ngOnInit(): void {
  }

}
