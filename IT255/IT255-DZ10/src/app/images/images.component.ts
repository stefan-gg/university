import { Component, Input, OnInit } from '@angular/core';
import { Image } from '../models/image/image';

@Component({
  selector: 'app-images',
  templateUrl: './images.component.html',
  styleUrls: ['./images.component.css']
})
export class ImagesComponent implements OnInit {
  @Input() image: Image

  constructor() {
  }

  ngOnInit(): void {
  }

}
