import { Injectable, Inject } from '@angular/core';
import {
    HttpClient,
} from '@angular/common/http';

import { map } from 'rxjs/operators';
import { Observable } from 'rxjs';

export const YOUTUBE_API_KEY =
    'AIzaSyAtXdsoo78YApWlh3ooVfjzREj9X9Ho8fQ';
export const YOUTUBE_API_URL =
    'https://www.googleapis.com/youtube/v3/search';

@Injectable()
export class YouTubeSearchService {
    constructor(
        private http: HttpClient,
        @Inject(YOUTUBE_API_KEY) private apiKey: string,
        @Inject(YOUTUBE_API_URL) private apiUrl: string
    ) { }

    search(query: string): Observable<any> {
        const params: string = [
            `q=${query}`,
            `key=${this.apiKey}`,
            `part=snippet`,
            `type=video`,
            `maxResults=5`
        ].join('&');
        const queryUrl = `${this.apiUrl}?${params}`;
        return this.http.get(queryUrl)
            .pipe(
                map((response: any) => response.items)
            );
        /*return this.http.get(queryUrl).map(response => {
            return <any>response['items'].map(item => {
                return new SearchResult({
                    id: item.id.videoId,
                    title: item.snippet.title,
                    description: item.snippet.description,
                    thumbnailUrl: item.snippet.thumbnails.high.url
                });
            });
        });*/
    }
}
