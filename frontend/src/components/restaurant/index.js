import React, { Component } from 'react';
import ReactLoading from 'react-loading';
import './index.css';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import RestaurantSlider from "./restaurantSlider";
import RestaurantDetails from "./restaurantDetails";
import RestaurantInfo from "./restaurantInfo";

import { fetchRestaurant } from "../../store/actions/restaurantActions";

class Restaurant extends Component {
  // constructor(props) {
  //     super(props);
  //
  //     this.state = {
  //         filter: '',
  //     }
  // }

  componentDidMount() {
      this.props.fetchRestaurant(this.props.match.params.restaurantId);
  }

  render() {
    console.log("Restaurant props", this.props);
    if (!this.props.restaurant) {
    return (
        <ReactLoading height={667} width={375} />
      )
    }

    return (
      <div>
        <RestaurantSlider/>
        <RestaurantDetails/>
          <div className="grid-container">
              <div className="restaurant-filter-container">Filter</div>
              <div className="restaurant-reviews-container">{ this.props.restaurant.reviews[0].content }</div>
              <RestaurantInfo className="restaurant-info-container">Info</RestaurantInfo>
          </div>
      </div>
    );
  }
}

const mapStateToProps = (state, props) => {
   const restaurant = state.restaurants.restaurant;
   const categories = state.restaurants.categories;

   return {
       restaurant,
       categories
   };
};

const mapDispatchToProps = (dispatch) => (
    {
        fetchRestaurant: (restaurantId) => dispatch(fetchRestaurant(restaurantId)),
    }
)

export default connect(mapStateToProps, mapDispatchToProps)(withRouter(Restaurant));
