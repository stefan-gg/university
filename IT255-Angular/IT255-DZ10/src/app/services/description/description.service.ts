import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Description } from 'src/app/models/description/description';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class DescriptionService {
  private API_KEY = "affe5ff6-89d7-40f0-8ed0-f42d39b4f045";
  private API_URL = "https://api.thecatapi.com/v1/breeds?limit=10";

  constructor(private httpClient: HttpClient) { }

  getCatBreeds(index: number): Observable<Description> {
    let url = `${this.API_URL}&api_key=${this.API_KEY}`;
    console.log("aaa");
    return this.httpClient.get(url).pipe(map((response: any) => this.makeDeskription(response, index)));
  }

  makeDeskription(item: any, index: number) {
    console.log(item[0].description);
    return new Description(item[index].description, item[index].origin, item[index].temperament);
  }

}
