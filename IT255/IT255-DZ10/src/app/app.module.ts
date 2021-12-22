import { NgModule, CUSTOM_ELEMENTS_SCHEMA, NO_ERRORS_SCHEMA } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ImagesComponent } from './images/images.component';
import { PagesComponent } from './pages/image-page/pages.component';
import { DescriptionsComponent } from './descriptions/descriptions.component';
import { DescriptionPageComponent } from './pages/description-page/description-page.component';

@NgModule({
  declarations: [
    AppComponent,
    ImagesComponent,
    PagesComponent,
    DescriptionsComponent,
    DescriptionPageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA, NO_ERRORS_SCHEMA]
})
export class AppModule { }
