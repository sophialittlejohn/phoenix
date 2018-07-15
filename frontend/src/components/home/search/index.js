import React, { Component } from 'react';
import './index.css';
import coverImg from "../../../images/thai.jpg"

class Search extends Component {
  handleSearch = e => {
      e.preventDefault();
  };

  render() {
    return (
      <div className="cover-img">
          <div className="form-wrapper-search overlay">
            <form onSubmit={this.handleSearch} className="search-form-style">
              <input className="search-style" type="text" placeholder="Search..." />
              <input className="submit-search search-style" type="submit" value="Search" />
            </form>
          </div>
          <img src={ coverImg } alt="cover-img" />
      </div>
    );
  }
}

export default Search;