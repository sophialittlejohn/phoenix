import React, { Component } from 'react';
import './index.css';
import { connect } from "react-redux"


class BestRatedRestaurants extends Component {
  render() {
    return (
      <div className="best-rest-container">
        <p>HELLO FROM BEST RATED RESTAURANTS</p>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  state
});

export default connect(mapStateToProps)(BestRatedRestaurants);