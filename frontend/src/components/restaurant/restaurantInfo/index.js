import "./index.css";
import "../index.css";
import React, { Component } from "react";
import ReactLoading from 'react-loading';
import {connect} from "react-redux";
import clockIcon from "../../../images/restaurant_icons/clock.svg";
import moneyIcon from "../../../images/restaurant_icons/money.svg";


class RestaurantInfo extends Component {

    writeReview = () => {
        console.log('Clicked write a reviews')
    }

    editData = () => {
        console.log('Clicked edit data')
    }

    render() {
    if (!this.props) {
      return (
        <ReactLoading height={667} width={375} />
      )
    }

    return (
      <div className="restaurant-info-container">
          <table className="restaurant-info-table">
              <tbody>
              <tr className="restaurant-info-row">
                <td className='hours-icon'><img src={ clockIcon } alt="clockIcon"/></td>
                <td>{ this.props.hours }</td>
              </tr>
              <tr className="restaurant-info-row">
                <td className='price-icon'><img src={ moneyIcon } alt="moneyIcon"/></td>
                <td>{ this.props.price }</td>
              </tr>
              </tbody>
          </table>
          <div className="write-review-button submit-button" onClick={ this.writeReview }>WRITE A REVIEW</div>
           <div className="edit-data-button submit-button" onClick={ this.editData }>EDIT DATA</div>
      </div>
    );
  }
}

const mapStateToProps = (state, props) => ({
    hours: state.restaurants.restaurant.opening_hours,
    price: state.restaurants.restaurant.price_level,
});

export default connect(mapStateToProps)(RestaurantInfo);
