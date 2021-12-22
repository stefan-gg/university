import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DescriptionPageComponent } from './pages/description-page/description-page.component';
import { PagesComponent } from './pages/image-page/pages.component';

const routes: Routes = [
  {path: 'images', component: PagesComponent},
  {path: 'descriptions', component: DescriptionPageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
