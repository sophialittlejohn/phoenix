import { combineReducers } from "redux"
import { restaurants } from "./restaurantReducers";

const getLoginCreds = (state = {}, action) => {
    switch (action.type) {
        case "LOGIN_CREDS":
            const newTokenState = {...state, tokens: action.payload};
            console.log("newTokenState ", newTokenState);
            return newTokenState;
        default:
            return state;
    }
};


const registerEmail = (state = {}, action) => {
    switch (action.type) {
        case "REGISTER":
            const newRegisterState = {...state, email: action.payload};
            console.log("newRegisterState: ", newRegisterState);
            return newRegisterState;
        case "REGISTER_VERIFICATION":
            const newVerificationState =  {...state, data: action.payload};
            console.log("newVerificationState: ", newRegisterState);
            return newVerificationState;
        default:
            return state;
    }
};

const rootReducer = combineReducers({
  getLoginCreds: getLoginCreds,
  registerEmail: registerEmail,
  restaurants,
});


export default rootReducer;
