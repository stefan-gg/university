import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Image } from 'src/app/models/image/image';
import { map } from "rxjs/operators";

@Injectable({
  providedIn: 'root'
})
export class ImagesService {
  private API_KEY = " affe5ff6-89d7-40f0-8ed0-f42d39b4f045";
  private API_URL = "https://api.thecatapi.com/v1/images/search?";

  constructor(private httpClient: HttpClient) { }

  getCatImages(): Observable<Image> {
    let url = `${this.API_URL}api_key=${this.API_KEY}`;
    return this.httpClient.get(url).pipe(map((response: any) => this.makeCatImage(response)));
  }

  makeCatImage(item: any) {
    return new Image(item[0].height, item[0].url, item[0].id, item[0].width)
  }
}
