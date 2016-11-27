import { combineReducers } from 'redux';
import { reducer as addRestaurant } from 'redux-form';

import { fetchRestaurantReducer } from './restaurant-reducer.js';
import placesReducer from './places-reducer';


const rootReducer = combineReducers({
  form: addRestaurant,
  restaurantFetch: fetchRestaurantReducer,
  placesReducer
});

export default rootReducer;
