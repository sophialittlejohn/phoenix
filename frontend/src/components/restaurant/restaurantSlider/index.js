import "./index.css";
import React, { Component } from "react";
import RestaurantOverlay from "./restaurantOverlay";
import ReactLoading from 'react-loading';
import {connect} from "react-redux";


class RestaurantSlider extends Component {

  render() {
    console.log('Slider props:', this.props);
    if (!this.props) {
      return (
        <ReactLoading height={667} width={375} />
      )
    }
    return (
      <div className="slider-container">
        <div className="restaurant-image">
          <img src={ this.props.img_src } alt=""/>
        </div>
        <RestaurantOverlay />
      </div>
    );
  }
}

const mapStateToProps = (state, props) => {
   return {
        img_src: state.restaurants.restaurant.image,
    };
};

export default connect(mapStateToProps)(RestaurantSlider);
