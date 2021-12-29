import { Action } from "@ngrx/store"
import { Smestaj } from "../models/smestaj.model"

export const DODAJ_SOBU = "DODAJ_SOBU"
export const OBRISI_SOBU = "OBRISI_SOBU"

export class DodajSobu implements Action {
    readonly type = DODAJ_SOBU

    constructor(public payload: Smestaj) { }
}

export class ObrisiSobu implements Action {
    readonly type = OBRISI_SOBU

    constructor(public payload: Smestaj) { }
}

export type Actions = DodajSobu | ObrisiSobu 