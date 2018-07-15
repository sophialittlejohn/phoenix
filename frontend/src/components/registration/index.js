import React, { Component } from "react";
import "./index.css"
import { connect } from "react-redux";
import { registerActionHelper } from "../../store/actions/index.js"
import {loginActionHelper} from "../../store/actions";

// todo figure out how to display message if email already exists

class Registration extends Component {
   constructor(props) {
    super(props);

    this.state = {
      submitted: false,
      email: ""
    };
  }

  // componentDidMount() {
  //      const email = this.props.match.params.email;
  // }

  handleEnterEmail = e => {
    const email = e.currentTarget.value;
    this.setState({ email });
  };

   handleSubmit = e => {
       e.preventDefault();
       this.setState({ submitted: true});
       this.props.dispatch(registerActionHelper(this.state));
   };

    render() {
        return (
            <div className="form-wrapper">
                <h2>Registration</h2>
                <div className="title-underline"> </div>
                {!this.state.submitted ?
                <form onSubmit={ this.handleSubmit } className="form-style">
                    <input
                        type="email"
                        name="email"
                        onChange={ this.handleEnterEmail}
                        placeholder="E-Mail Address"
                        className="input-style"
                        />
                    <input type="submit" value="Register" className="submit-form"/>
                </form>
                :
                <p className="monkey-text">
                  Thanks for your registration.
    Our hard working monkeys are preparing a digital message called E-Mail that will be sent to you soon. Since monkeys
                    aren't good in writing the message could end up in you junk folder. Our apologies for any
                    inconvenience.
                </p>
                }
                </div>
        )
    }
}


const mapStateToProps = state => ({
  state
});

export default connect(mapStateToProps)(Registration);
