import "./index.css";
import React, { Component } from "react";
import ReactLoading from 'react-loading';
import {connect} from "react-redux";
import { fetchRestaurantReviews } from "../../store/actions/reviewsActions";
import {fetchRestaurant} from "../../store/actions/restaurantActions";


class Reviews extends Component {

    componentDidMount() {
      this.props.fetchRestaurantReviews(this.props.match.params.restaurantId);
  }

    render() {
    if (!this.props) {
      return (
        <ReactLoading height={667} width={375} />
      )
    }

    return (
      <div className="review-container">
          hello from reviews container
      </div>
    );
  }
}

const mapStateToProps = (state, props) => (state);


const mapDispatchToProps = (dispatch) => (
    {
        fetchRestaurantReviews: (restaurantId) => dispatch(fetchRestaurantReviews(restaurantId)),
    }
)

export default connect(mapStateToProps, mapDispatchToProps)(Reviews);
