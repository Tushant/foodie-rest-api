const initialState = {
  fetching: false,
  fetched: true,
  restaurants: [],
  error: null,
};

export const fetchRestaurantReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'FETCH_RESTAURANT_START':
      return { ...state, fetching: true };
    case 'FETCH_RESTAURANT_ERROR':
      return { ...state, fetching: false, error: action.payload };
    case 'RECIEVE_RESTAURANT':
      return { ...state, fetching: false, fetched: true, restaurants: action.payload };
    default:
      return state;
  }
};
