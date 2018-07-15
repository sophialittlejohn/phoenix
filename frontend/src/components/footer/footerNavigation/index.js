import React, { Component } from "react";
import "./index.css"
import instagram from "../../../images/social_icons/instagram.svg"
import facebook from "../../../images/social_icons/facebook.svg";
import twitter from "../../../images/social_icons/twitter.svg";
import googleplus from "../../../images/social_icons/googleplus.svg";


class FooterNavigation extends Component {
    render() {
        return (
            <div className="footer-nav">
                <a href="#" className="footer-nav-item">About Us</a>
                <a href="#" className="footer-nav-item">Press</a>
                <a href="#" className="footer-nav-item">Blog</a>
                <a href="#" className="footer-nav-item">iOS</a>
                <a href="#" className="footer-nav-item">Android</a>

                <a href="#" className="footer-social-nav"><img src={ instagram } alt="instagram" className="social-handle"/></a>
                <a href="#" className="footer-social-nav"><img src={ facebook } alt="facebook" className="social-handle"/></a>
                <a href="#" className="footer-social-nav"><img src={ googleplus } alt="googleplus" className="social-handle"/></a>
                <a href="#" className="footer-social-nav"><img src={ twitter } alt="twitter" className="social-handle"/></a>
            </div>
        )
    }
}


export default FooterNavigation;