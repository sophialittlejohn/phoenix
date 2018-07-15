import {GET_REVIEWS} from "../constants";

const initialState = {};

export const reviews = (state = initialState, action) => {
    switch(action.type) {
        case GET_REVIEWS:
            const { reviews } = action.payload;
            return {...state, reviews};
        default:
            return state;
    }
};
