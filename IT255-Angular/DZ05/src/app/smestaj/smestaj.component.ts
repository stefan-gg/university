import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { SmestajService } from '../services/smestaj.service';
import { Smestaj } from '../models/smestaj.model';
import { AppState } from '../app.state';
import { Store } from '@ngrx/store';

@Component({
  selector: 'app-smestaj',
  templateUrl: './smestaj.component.html',
  styleUrls: ['./smestaj.component.css']
})
export class SmestajComponent implements OnInit {
  smestaji: Smestaj[]
  brojRezervisanihDana : number;
  @Output() deleteSmestaj = new EventEmitter();
  @Input() smestaj: Smestaj;

  constructor(private smestajService: SmestajService, private store: Store<AppState>) {
    this.smestaj = new Smestaj("", "", "", 0, 1);
    this.brojRezervisanihDana = 1;
    this.store.select("smestaji").subscribe(smestaji => this.smestaji = [...smestaji]);
  }

  public obrisi(): void {
    this.deleteSmestaj.emit(this.smestaj);
  }

  dodajJednuNoc(): void {
    this.brojRezervisanihDana += 1;
  }

  otkaziJednuNoc(): void {
    if (this.brojRezervisanihDana > 1) {
      this.brojRezervisanihDana -= 1;
    }
  }

  izracunajCenu(): number{
    return this.smestajService.getCenaSmestaja(this.brojRezervisanihDana, this.smestaj.cenaSobe);
  }

  ngOnInit(): void {
  }

}



