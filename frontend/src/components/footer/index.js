import React, { Component } from "react";
import "./index.css"
import FooterNavigation from "./footerNavigation";


// todo: fix maxwidth error for footer!
class Footer extends Component {
    render() {
        return (
            <div className="footer-style">
                <FooterNavigation />
                <div className="copy-right">
                    © Copyright Luna 2018
                </div>
            </div>
        )
    }
}


export default Footer;