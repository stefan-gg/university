import { Component, Input, OnInit } from '@angular/core';
import { Description } from '../models/description/description';

@Component({
  selector: 'app-descriptions',
  templateUrl: './descriptions.component.html',
  styleUrls: ['./descriptions.component.css']
})
export class DescriptionsComponent implements OnInit {
  @Input() description: Description

  constructor() { }

  ngOnInit(): void {
  }

}
