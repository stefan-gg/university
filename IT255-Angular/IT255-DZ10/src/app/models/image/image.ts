export class Image {
    height: number;
    imageUrl: string;
    id: string;
    width: number;

    constructor(height: number, imageUrl: string, id: string, width: number,) {
        this.height = height;
        this.imageUrl = imageUrl;
        this.id = id;
        this.width = width;
    }
}
