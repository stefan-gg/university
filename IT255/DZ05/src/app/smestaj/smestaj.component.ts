import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import {Smestaj} from './smestaj.model';

@Component({
  selector: 'app-smestaj',
  templateUrl: './smestaj.component.html',
  styleUrls: ['./smestaj.component.css']
})
export class SmestajComponent implements OnInit {
  
  @Output() deleteSmestaj: EventEmitter<Smestaj>;
  @Input() smestaj: any;
  
  constructor() {
    this.deleteSmestaj = new EventEmitter();
  }

  public obrisi(): void {
    this.deleteSmestaj.emit(this.smestaj);
  }

  ngOnInit(): void {
  }

}
  

  
