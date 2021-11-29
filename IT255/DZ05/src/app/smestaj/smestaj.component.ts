import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { SmestajService } from '../services/smestaj.service';
import { Smestaj } from './smestaj.model';

@Component({
  selector: 'app-smestaj',
  templateUrl: './smestaj.component.html',
  styleUrls: ['./smestaj.component.css']
})
export class SmestajComponent implements OnInit {

  @Output() deleteSmestaj = new EventEmitter();
  @Input() smestaj: Smestaj;

  constructor(private smestajService: SmestajService) {
    this.smestaj = new Smestaj("", "", "", 0, 1);
  }

  public obrisi(): void {
    this.deleteSmestaj.emit(this.smestaj);
  }

  dodajJednuNoc(): void {
    this.smestaj.brojRezervisanihDana += 1;
  }

  otkaziJednuNoc(): void {
    if (this.smestaj.brojRezervisanihDana > 1) {
      this.smestaj.brojRezervisanihDana -= 1;
    }
  }

  izracunajCenu(): number{
    return this.smestajService.getCenaSmestaja(this.smestaj.brojRezervisanihDana, this.smestaj.cenaSobe);
  }

  ngOnInit(): void {
  }

}



