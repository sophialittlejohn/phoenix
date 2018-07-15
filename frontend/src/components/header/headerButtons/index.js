import "./index.css";
import React, { Component } from "react";
import { Link } from "react-router-dom";


class HeaderButtons extends Component {
    handleLogin = () => {
      // todo: send the user to the login page
        console.log("clicked login")
    };

    render() {
        return (
            <span>
                <Link to="/registration">
                    <button className="sign-up-button">SIGNUP</button>
                </Link>
                <Link to="/login">
                    <button onClick={ this.handleLogin } className="login-button">LOGIN</button>
                </Link>
            </span>
        )
    }
}

export default HeaderButtons;