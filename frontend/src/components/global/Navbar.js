import React,{ Component } from 'react';
import { BrowserRouter as Router, Link, Match } from 'react-router';

import AddRestaurant from '../add/AddRestaurant';
import App from '../app';

export default class Navbar extends Component{
  constructor(props){
    super(props);
    this.state = { open: false };

  }
  handleToggle = () => this.setState({open: !this.state.open});

  handleClose = () => this.setState({open: false});

  render(){
  return(
    <nav className="nav">
        
        {/* <Router>
          <Link to='/restaurant'>Home</Link>
          <Link to='/addrestaurant'>Add Restaurant</Link>
          <Match exactly pattern="/restaurant" component={App} />
          <Match pattern="/addrestaurant" component={AddRestaurant} />
        </Router> */}
    </nav>
  );
}
}
