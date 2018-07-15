import "./index.css";
import React, { Component } from "react";
import logo from "../../images/logo.svg";
import HeaderButtons from "./headerButtons";
import HeaderNavigation from "./headerNavigation"

class Header extends Component {

  render() {
    return (
      <div className="header-container">
        <div className="header-content">
          <img src={logo} alt="luna-logo" className="logo" />
          <HeaderButtons />
          <HeaderNavigation />
        </div>
      </div>
    );
  }
}

export default Header;

// button colors: #E47D31 (orange)
