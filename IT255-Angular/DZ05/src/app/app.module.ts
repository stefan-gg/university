import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SmestajComponent } from './smestaj/smestaj.component';
import { FormaComponent } from './forma/forma.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { SmestajService } from './services/smestaj.service';
import { SingleSmestajComponent } from './single-smestaj/single-smestaj.component';
import { SmestajiComponent } from './smestaji/smestaji.component';
import { StoreModule } from '@ngrx/store';
import { reducers } from './app.state';

@NgModule({
  declarations: [
    AppComponent,
    SmestajComponent,
    FormaComponent,
    SingleSmestajComponent,
    SmestajiComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    StoreModule.forRoot(reducers)
  ],
  providers: [SmestajService],
  bootstrap: [AppComponent]
})
export class AppModule { }
