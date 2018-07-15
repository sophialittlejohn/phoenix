import React, { Component } from 'react';
import './index.css';
import Search from "./search"
import BestRatedRestaurants from "./bestRatedRestaurants"

class Home extends Component {
  render() {
    return (
      <div >
        <div>
           <Search />
        </div>

        {/*<div>*/}
          {/*<BestRatedRestaurants />*/}
        {/*</div>*/}
      </div>

    );
  }
}

export default Home;