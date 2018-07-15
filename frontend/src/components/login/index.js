import React, {Component} from "react"
import "./index.css";
import {connect} from "react-redux";
import {loginAction, loginActionHelper} from "../../store/actions";


class Login extends Component {
    constructor(props) {
        super(props);

        this.state = {
            username: "",
            password: "",
        };
    }


    handleEnterUsername = e => {
        this.setState({ username: e.currentTarget.value})
    };

    handleEnterPassword = e => {
        this.setState({ password: e.currentTarget.value})
    };

    handleSubmit = e => {
        e.preventDefault();
        this.props.dispatch(loginActionHelper(this.state)).then((data) => {
            if (data) {
                if (data.username) {
                  alert(`Username: ${data.username}`);
                } else if (data.password) {
                    alert(`Password: ${data.password}`);
                } else if (data.non_field_errors) {
                    alert(`Field: ${data.non_field_errors}`);
                }
            } else {
                this.props.history.push("/")
            }

        })
    };

    render() {
        console.log("IN THE LOGIN RENDER: ", this);
        return (
            <div className="form-wrapper">
                <h2>Login</h2>
                <div className="title-underline"> </div>

                <form onSubmit={this.handleSubmit} className="form-style">
                    <input
                        type="text"
                        onChange={this.handleEnterUsername}
                        placeholder="Username"
                        className="input-style"
                        value={this.state.username}/>
                    <input
                        type="Password"
                        onChange={this.handleEnterPassword}
                        placeholder="Password"
                        className="input-style"
                        value={this.state.password}/>

                    <input
                        type="submit"
                        value="Login"
                        className="submit-form"/>
                </form>

            </div>
        )
    }
}


const mapStateToProps = state => ({
    state
});

export default connect(mapStateToProps)(Login);