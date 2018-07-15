import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import registerServiceWorker from './registerServiceWorker';
import { Provider } from "react-redux";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import store from "./store";
import Home from "./components/home/index.js"
import Header from "./components/header";
import Footer from "./components/footer";
import Registration from "./components/registration";
import RegistrationVerification from "./components/registration/registrationVerification"
import Login from "./components/login";
import Restaurant from "./components/restaurant";
import {fetchCategories} from "./store/actions/restaurantActions";

store.dispatch(fetchCategories());

ReactDOM.render(
    <Provider store={ store }>
      <Router>
        <Switch>
        <div>
          <Header/>
          <Route exact path="/" component={ Home } />
          <Route exact path="/registration" component={ Registration } />
          <Route exact path="/registration/verification/:email/:code" component={ RegistrationVerification } />
          <Route exact path="/login" component={ Login } />
          <Route exact path="/restaurants/:restaurantId" component={ Restaurant } />
          <Footer/>
        </div>
        </Switch>
      </Router>
    </Provider>,
    document.getElementById('root'));
registerServiceWorker();

