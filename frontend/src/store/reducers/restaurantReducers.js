import {GET_CATEGORIES, GET_RESTAURANT} from '../constants';

const initialState = {};

export const restaurants = (state = initialState, action) => {
    switch(action.type) {
        case GET_RESTAURANT:
            const { restaurant } = action.payload;
            return {...state, restaurant};
        case GET_CATEGORIES:
            const { categories } = action.payload;
            return {...state, categories};
        default:
            return state;
    }
};
