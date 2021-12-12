import { Component } from '@angular/core';
import { YouTubeSearchService } from './components/video-box/you-tube-search.service';
import { Video } from './models/video';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  title = 'it255';
  public videos: Video[] = [];
  private _links: string[] = [
    'American Idiot Green Day',
    'Holiday Green Day',
    'Party Monster The Weeknd',
    'Boulevard Of Broken Dreams Green Day',
    '21 Guns Green Day',
    'P2 - Lil Uzi'
  ];

  constructor(private youTubeSearchService: YouTubeSearchService) {
    for (let i = 0; i < 6; i++) {
      this.videos.push(new Video(this._generateString(3), this._generateString(100), 'https://www.youtube.com/embed/' + this._links[i], this._generateRandomLength()))
    }
  }

  private _generateString(length) {
    let result = '';
    let characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let charactersLength = characters.length;
    for (let i = 0; i < length; i++) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
  }

  private _generateRandomLength(): number {
    return Math.floor(Math.random() * 240);
  }

  public deleteVideo(video: Video) {
    this.videos = this.videos.filter(item => {
      return item.title !== video.title
    })
  }

  public sort(type: string) {
    this.videos.sort((a, b) => {
      return type == 'asc' ? a.length - b.length : b.length - a.length;
    });
  }

  public updateVideo(video: Video) {
    //let index = this.videos.findIndex(i => i.title === video.title);
    //this.videos[index].title = this._generateString(6);
    //this.videos[index].description = this._generateString(50);
  }

  public nadjiVideo(naziv: string) {
    this.youTubeSearchService.search(naziv)
      .subscribe((items: any) => {
        this.videos = items.map(item => {
          return {
            title: item.snippet.title,
            link: item.snippet.thumbnails.high.url,
            description: item.snippet.description,
            length: this._generateRandomLength()
          };
        });
      });
  }


  public addVideo() {
    let video = this._links[Math.floor(Math.random() * this._links.length)]
    this.nadjiVideo(video);
    //this.videos.unshift(new Video(/*this._generateString(3)*/"Naslov klipa", /*this._generateString(100)*/"Opis klipa", 'https://www.youtube.com/embed/' /*+ this._links[Math.floor(Math.random() * this._links.length - 1)]*/, 100/*this._generateRandomLength()*/))
  }

}
