import { ActionReducerMap } from "@ngrx/store";
import { Smestaj } from "./models/smestaj.model";
import { smestajReducer } from "./reducers/smestaj.reducer";

export interface AppState {
    readonly smestaji: Smestaj[];
};

export const reducers: ActionReducerMap<AppState, any> = {
    smestaji: smestajReducer
}