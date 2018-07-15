const baseUrl = 'http://phoenix.propulsion-learn.ch/backend/';

export const loginAction = ( tokens ) => {
    return {
        type: "LOGIN_CREDS",
        payload: tokens
    }
};

export const loginActionHelper = data => (dispatch, getState) => {
    const headers = new Headers({
            "Content-Type": "application/json"
        });
        const config = {
            method: "POST",
            headers: headers,
            body: JSON.stringify(data)
        };

    return fetch(`${baseUrl}api/auth/token/`, config)
        .then(response => {
            if (response.status === 400) {
                console.log("IN THE LOGIN ACTION ", response);
                return response.json().then((errors) => {
                    return errors;
                })
            } else {
                response.json().then((token) => {
                    localStorage.setItem("token", JSON.stringify(token.access));
                    console.log(token);
                    dispatch(loginAction(token));
                })
            }
        })
};


export const registerAction = email => {
    return {
        type: "REGISTER",
        payload: email
    }
};

export const registerActionHelper = email => (dispatch, getState) => {
    const headers = new Headers({
        "Content-Type": "application/json"
    });
    const config = {
        method: "POST",
        headers,
        body: JSON.stringify(email)
    };

    return fetch(`${baseUrl}api/registration/`, config)
        .then(response => {
            if (response.status === 400) {
                return response.json().then((errors) => {
                    console.log("Errors: ", errors);
                    return errors
                })
            } else {
                response.json().then((email) => {
                    console.log("IN THE FETCHER", email);
                    dispatch(registerAction(email));
                })
            }
        })
};


export const verificationAction = data => {
    return {
        type: "REGISTER_VERIFICATION",
        payload: { data }
    }
};

export const verificationActionHelper = data => (dispatch, getState) => {
    const headers = new Headers({
        "Content-Type": "application/json"
    });
    const config = {
        method: "POST",
        headers,
        body: JSON.stringify(data)
    };

    return fetch(`${baseUrl}api/registration/validate/`, config)
            .then(response => {
            if (response.status === 400) {
                return response.json().then((errors) => {
                    console.log("Errors: ", errors);
                    return errors
                })
            } else {
                response.json().then((data) => {
                    console.log("IN THE FETCHER VERIFICATION", data);
                    dispatch(verificationAction(data));
                })
            }
        })
};
