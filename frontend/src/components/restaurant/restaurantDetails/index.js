import "./index.css";
import React, { Component } from "react";
import RestaurantContacts from "./restaurantContacts";
import RestaurantMap from './restaurantMap';

class RestaurantDetails extends Component {
    render() {
    return (
      <div className="restaurant-details-container">
          <RestaurantMap/>
          <RestaurantContacts/>
      </div>
    );
  }
}

export default RestaurantDetails;
