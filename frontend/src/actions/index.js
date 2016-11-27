import axios from 'axios';

export function fetchRestaurant() {
  return (dispatch) => {
    dispatch({ type: 'FETCH_RESTAURANT_START' });
    axios.get('/api/restaurant')
    .then((response) => {
      dispatch({ type: 'RECIEVE_RESTAURANT', payload: response.data });
    })
    .catch((err) => {
      dispatch({ type: 'FETCH_RESTAURANT_ERROR', payload: err });
    });
  };
}
