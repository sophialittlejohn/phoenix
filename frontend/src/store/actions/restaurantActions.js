import {
    baseUrl, GET_CATEGORIES,
    GET_RESTAURANT
} from '../constants';

const getRestaurant = (restaurant) => (
    {
        type: GET_RESTAURANT,
        payload: { restaurant }
    }
)

const getCategories = (categories) => ({
    type: GET_CATEGORIES,
    payload: { categories }
});

export const fetchRestaurant = (restaurantId) => (dispatch, getState) => {
    console.log('in fetch restaurant');
    const headers = new Headers({
            "Content-Type": "application/json"
        });
        const config = {
            method: "GET",
            headers: headers,
        };

    return fetch(`${baseUrl}api/restaurants/${restaurantId}/`, config)
        .then(response => response.json())
        .then(restaurant => {
            dispatch(getRestaurant(restaurant));
        })
};

export const fetchCategories = () => (dispatch, getState) => {
    const headers = new Headers({
            "Content-Type": "application/json"
        });
        const config = {
            method: "GET",
            headers: headers,
        };

    return fetch(`${baseUrl}api/category/list/`, config)
        .then(response => response.json())
        .then(categories => {
            dispatch(getCategories(categories));
        })
}
