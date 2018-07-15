import React, { Component } from "react";
import "./index.css";
import { Link } from "react-router-dom"


class HeaderNavigation extends Component {

    handleNavClick = (e) => {
        // todo:  change the clicked span to class selected
        console.log(e.target);
    };

    render () {
        return (
            <span className="navigation">
                <a href="#" className={`nav-item`}>Profile</a>
                <a href="#" className={`nav-item`}>Search</a>
                <Link to="/">
                    <span className={`selected nav-item`}>Home</span>
                </Link>
            </span>
        )
    }
}

export default HeaderNavigation;