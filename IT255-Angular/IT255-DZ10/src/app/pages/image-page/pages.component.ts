import { Component, OnInit } from '@angular/core';
import { ImagesComponent } from '../../images/images.component';
import { Image } from '../../models/image/image';
import { ImagesService } from '../../services/images/images.service';

@Component({
  selector: 'app-pages',
  templateUrl: './pages.component.html',
  styleUrls: ['./pages.component.css']
})
export class PagesComponent implements OnInit {
  images: Image[] = []

  constructor(private image: ImagesService) { 
    for (let index = 0; index < 10; index++) {
      this.image.getCatImages().subscribe(item => this.images.push(item));
    }
  }

  ngOnInit(): void {
  }

}
