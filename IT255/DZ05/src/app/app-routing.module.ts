import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SingleSmestajComponent } from './single-smestaj/single-smestaj.component';
import { SmestajComponent } from './smestaj/smestaj.component';
import { SmestajiComponent } from './smestaji/smestaji.component';

const routes: Routes = [
  {path:"smestaj/:id", component: SingleSmestajComponent},
  {path:"smestaji", component: SmestajiComponent},
  { path: '**', redirectTo: '/smestaji'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
