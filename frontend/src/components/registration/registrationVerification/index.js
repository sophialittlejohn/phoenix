import React, {Component} from "react";
import "./index.css"
import {connect} from "react-redux";

import { verificationActionHelper } from "../../../store/actions/index.js"


class RegistrationVerification extends Component {
    constructor(props) {
        super(props);

        this.state = {
            submitted: false,
            email: this.props.match.params.email,
            code: parseInt(this.props.match.params.code),
            username: "",
            password: "",
            password_repeat: "",
            location: "",
        };
    }

    handlePassword = e => {
        const password = e.currentTarget.value;
        this.setState({ password });
    };

    handlePasswordRepeat = e => {
        const password_repeat = e.currentTarget.value;
        this.setState({ password_repeat });
    };

    handleUsername = e => {
        const username = e.currentTarget.value;
        this.setState({ username });
    };

    handleLocation = e => {
        const location = e.currentTarget.value;
        this.setState({ location });
    };

    handleSubmit = e => {
        e.preventDefault();
        this.setState({ submitted: true });
        this.props.dispatch(verificationActionHelper(this.state)).then((data) => {
            if (data) {
                alert(data)
            } else {
                this.props.history.push("/")
            }
        })
    };

    form = (email, code) => {
        return (
        <div className="form-wrapper">
                <h2>Verification</h2>
                <div className="title-underline"> </div>
                {!this.state.submitted ?
                    <form className="verification-form-style" onSubmit={this.handleSubmit}>
                    <input
                        className="input-style"
                        type="email"
                        value={email}
                    />
                    <input
                        className="input-style"
                        type="number"
                        value={code}
                    />
                    <input
                        className="input-style"
                        type="text"
                        placeholder="Username"
                        onChange={this.handleUsername}
                        value={this.state.value}
                    />
                    <input
                        className="input-style"
                        type="text"
                        placeholder="Location"
                        onChange={this.handleLocation}
                        value={this.state.value}
                    />
                    <input
                        className="input-style"
                        type="password"
                        placeholder="Password"
                        onChange={this.handlePassword}
                        value={this.state.value}
                    />
                    <input
                        className="input-style"
                        type="password"
                        placeholder="Password repeat"
                        onChange={this.handlePasswordRepeat}
                        value={this.state.value}
                    />
                    <input
                        type="submit"
                        value="Finish registration"
                        className="submit-form"/>
                </form> :
                    <p>Thanks for registering.</p> }
            </div>
        )};

    render() {
        const email = this.props.match.params.email;
        const code = this.props.match.params.code;
        return (
            this.form(email, code)
        )
    }
}

const mapStateToProps = state => {
    console.log("FROM THE MSTP: ", state);
    return {
      email: state.registerEmail
    }
};
export default connect(mapStateToProps)(RegistrationVerification)
