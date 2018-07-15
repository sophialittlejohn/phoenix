import "./index.css";
import React, { Component } from "react";
import ReactLoading from 'react-loading';
import {connect} from "react-redux";
import placeholderIcon from "../../../../images/restaurant_icons/placeholder.svg";
import phoneIcon from "../../../../images/restaurant_icons/phone.svg";
import webIcon from "../../../../images/restaurant_icons/web.svg";

class RestaurantContacts extends Component {
    render() {
    if (!this.props) {
      return (
        <ReactLoading height={667} width={375} />
      )
    }

    return (
      <div className="restaurant-contacts-container">
           <table className="restaurant-contacts-table">
              <tbody>
              <tr className="restaurant-contact-row">
                <td className='contact-icon'><img src={ placeholderIcon } alt="placeholderIcon"/></td>
                <td>{ this.props.street }</td>
              </tr>
              <tr className="restaurant-contact-row">
                <td className='contact-icon'><img src={ phoneIcon } alt="phoneIcon"/></td>
                <td>{ this.props.phone }</td>
              </tr>
              <tr className="restaurant-contact-row">
                <td className='contact-icon'><img src={ webIcon } alt="webIcon"/></td>
                <td>{ this.props.website ? this.props.website : 'no website'}</td>
              </tr>
              </tbody>
            </table>
      </div>
    );
  }
}

const mapStateToProps = (state, props) => ({
    street: state.restaurants.restaurant.street,
    phone: state.restaurants.restaurant.phone_number,
    website: state.restaurants.restaurant.website,
});

export default connect(mapStateToProps)(RestaurantContacts);
