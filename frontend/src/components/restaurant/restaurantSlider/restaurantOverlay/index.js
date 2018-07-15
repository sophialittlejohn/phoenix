import "./index.css";
import React, { Component } from "react";
import ReactLoading from 'react-loading';
import {connect} from "react-redux";

class RestaurantOverlay extends Component {

  render() {
    console.log("Overlay props", this.props);
    if (!this.props) {
      return (
        <ReactLoading height={667} width={375} />
      )
    }

    return (
      <div className="overlay-container">
        <div className="overlay-content">
         <div className="restaurant-name">{ this.props.name }</div>
         <div className="restaurant-category">{ this.props.category ? this.props.category : 'No category' }</div>
         <div className="restaurant-star-rating">{'Rating'}
            <span className="restaurant_reviews_number">{ this.props.reviews } reviews</span>
         </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state, props) => {
    return {
        name: state.restaurants.restaurant.name,
        category: state.restaurants.categories.find(
            cat => cat.id === state.restaurants.restaurant.category).name,
        reviews: state.restaurants.restaurant.reviews.length,
    };
};

export default connect(mapStateToProps)(RestaurantOverlay);
