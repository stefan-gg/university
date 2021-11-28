import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { AbstractControl, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Smestaj } from '../smestaj/smestaj.model';

@Component({
  selector: 'app-forma',
  templateUrl: './forma.component.html',
  styleUrls: ['./forma.component.css']
})
export class FormaComponent implements OnInit {

  @Output() dodajSmestaj = new EventEmitter();
  forma: FormGroup
  imeHotela: AbstractControl
  brojSoba: AbstractControl
  opisHotela: AbstractControl

  constructor(formBuilder: FormBuilder) {
    this.forma = formBuilder.group({ 
      'imeHotela': ['', Validators.compose([Validators.required, Validators.pattern(/^([ \u00c0-\u01ffa-zA-Z'\-])+$/)])],
      'brojSoba': ['',Validators.compose([Validators.required, Validators.pattern(/^\d+$/)])],
      'opisHotela': ['', Validators.required] 
    })

    this.imeHotela = this.forma.controls['imeHotela'];
    this.brojSoba = this.forma.controls['brojSoba'];
    this.opisHotela = this.forma.controls['opisHotela'];

    this.opisHotela.valueChanges.subscribe(
      (opis: string) => {
        if(opis.length < 6){
          console.log("Opis ima  : " + opis.length + " slova, a minimum je 6")
        }
      }
    )
  }

  ngOnInit(): void {
  }

  onSubmit(forma: any): void{
    this.dodajSmestaj.emit(new Smestaj(forma.imeHotela, forma.brojSoba, forma.opisHotela));
    console.log("nije gore moze lose");
  }
}
