import { Injectable } from "@angular/core";

@Injectable()
export class SmestajService {
    constructor() { }

    getCenaSmestaja(brojNoci: number, cenaPoNoci: number): number {
        return brojNoci * cenaPoNoci;
    }
}