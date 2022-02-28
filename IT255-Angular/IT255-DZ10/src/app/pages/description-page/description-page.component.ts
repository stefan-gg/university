import { Component, OnInit } from '@angular/core';
import { Description } from 'src/app/models/description/description';
import { DescriptionService } from 'src/app/services/description/description.service';

@Component({
  selector: 'app-description-page',
  templateUrl: './description-page.component.html',
  styleUrls: ['./description-page.component.css']
})
export class DescriptionPageComponent implements OnInit {
  descriptions: Description[] = [];

  constructor(private descriptionService: DescriptionService) {
    for (let index = 0; index < 10; index++) {
      this.descriptionService.getCatBreeds(index).subscribe(item => this.descriptions.push(item));
    }
  }


  ngOnInit(): void {
  }

}
