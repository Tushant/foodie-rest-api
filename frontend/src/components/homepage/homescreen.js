import React, { Component, PropTypes } from 'react';
import { Icon } from 'semantic-ui-react';
import { BrowserRouter as Router, Match, Link } from 'react-router';

import AddRestaurant from '../add/add-restaurant';
import Content from './Content';
import Banner from './banner';

const routes = [
  {
      pattern: '/restaurant',
      component: () => <Content />
  },
  { pattern: '/addrestaurant',
    component: () => <AddRestaurant />
  }
];

class HomeScreen extends Component {
    render() {
        return (
          <Router>
            <div className="ui">
              <Match pattern='/restaurant' component={Content} />
              <Match pattern='/addrestaurant' component={AddRestaurant} />
            </div>
          </Router>
        );
    }
}

export default HomeScreen;
