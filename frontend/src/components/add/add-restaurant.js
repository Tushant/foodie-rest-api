import React, { Component } from 'react';
import Banner from '../homepage/banner';
import RestaurantForm from './restaurant-form';

class AddRestaurant extends Component {
  render() {
    return (
    	<div className="add-restaurant">
            <Banner />
    		<RestaurantForm />
        </div>
    );
  }
}

export default AddRestaurant;