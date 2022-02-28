import { Smestaj } from "../models/smestaj.model";
import * as SmestajActions from '../actions/smestaj.actions'

const initialState: Smestaj = {
    imeHotela: "Hotel 123",
    opisHotela: "Opis hotela 123",
    brojSoba: "200",
    cenaSobe: 1000,
    brojRezervisanihDana: 10
}

export function smestajReducer(state: Smestaj[] = [initialState], action: SmestajActions.Actions) {
    switch (action.type) {
        case SmestajActions.DODAJ_SOBU:
            return [...state, action.payload];
        case SmestajActions.OBRISI_SOBU:
            let newState = [...state]
            let index = newState.indexOf(action.payload)
            newState.splice(index, 1)
            return newState
        default:
            return state;
    }
}