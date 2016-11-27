import React, {PropTypes} from 'react';
import axios from 'axios';

import PersonalInfo from './PersonalInfo';
import Menu from './Menu';

const styles = {
  headline: {
    fontSize: 24,
    paddingTop: 16,
    marginBottom: 12,
    fontWeight: 300,
  },
  slide: {
    padding: 10,
  },
};

export default class RestaurantDetail extends React.Component {
  constructor(props) {
    super(props);
    this.state = {restaurant:[], slideIndex: 0};
  }

  fetchSingleRestaurantFromServer(){
    console.log('props',this.props.params.slug);
    axios.get(`/api/restaurant/${this.props.params.slug}`)
    .then((response) => {
      this.setState({restaurant:response.data});
    })
    .catch(error => {
      console.log(error)
    })
  }

  componentDidMount(){
    this.fetchSingleRestaurantFromServer();
  }

  handleChange = (value) => {
   this.setState({
     slideIndex: value,
   });
 }

  render() {
    const restaurant = this.state.restaurant;
    return (
      <div className="container-fluid" style={{ paddingLeft:'0', paddingRight:'0' }}>
        <div className="restaurant-header">
          <img src={restaurant.image} className="responsive-img" alt={restaurant.name} style={{ height:'400px', width:'100%'}} />
        </div>
      </div>
    );
  }
}
