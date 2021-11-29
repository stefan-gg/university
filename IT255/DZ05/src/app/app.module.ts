import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SmestajComponent } from './smestaj/smestaj.component';
import { FormaComponent } from './forma/forma.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { SmestajService } from './services/smestaj.service';

@NgModule({
  declarations: [
    AppComponent,
    SmestajComponent,
    FormaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [SmestajService],
  bootstrap: [AppComponent]
})
export class AppModule { }
