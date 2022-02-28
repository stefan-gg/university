export class Video {
    title: string;
    description: string;
    link: string;
    length: number;
    
    constructor(title: string, description: string, link: string, length: number) {
        this.title = title;
        this.description = description;
        this.link = link;
        this.length = length;
    }
}
