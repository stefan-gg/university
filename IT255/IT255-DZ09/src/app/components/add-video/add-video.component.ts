import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Video } from 'src/app/models/video';

@Component({
  selector: 'app-add-video',
  templateUrl: './add-video.component.html',
  styleUrls: ['./add-video.component.scss']
})
export class AddVideoComponent implements OnInit {
  public videoForm: FormGroup;
  @Output() videoToAdd: EventEmitter<Video>;
  constructor() {
    this.videoToAdd = new EventEmitter();
   }

  ngOnInit() {
    this.initForm();
  }

  public initForm() {
    this.videoForm = new FormGroup({
      title: new FormControl('', [
        Validators.required
      ]),
      link: new FormControl('', [
        Validators.required
      ]),
      description: new FormControl('', [
        Validators.required
      ])
    });
    
  }

  public submitForm() {
    let title = this.videoForm.get('title').value;
    let link = this.videoForm.get('link').value;
    let description = this.videoForm.get('description').value;
    let video = new Video(title, description, link, length);
    this.videoToAdd.emit(video);
  }
}
