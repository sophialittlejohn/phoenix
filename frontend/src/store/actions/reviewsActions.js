import {
    baseUrl,
    GET_REST_REVIEWS
} from '../constants';

const getRestaurantReviews = (reviews) => (
    {
        type: GET_REST_REVIEWS,
        payload: { reviews }
    }
)


export const fetchRestaurantReviews = (restaurantId) => (dispatch, getState) => {
    console.log('in fetch restaurant reviews');
    const headers = new Headers({
            "Content-Type": "application/json"
        });
        const config = {
            method: "GET",
            headers: headers,
        };

    return fetch(`${baseUrl}api/reviews/restaurant/${restaurantId}/`, config)
        .then(response => response.json())
        .then(reviews => {
            dispatch(getRestaurantReviews(reviews));
        })
};
