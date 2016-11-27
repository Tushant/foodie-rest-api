import React,{Component, PropTypes} from 'react';
import {Link} from 'react-router';

export default class GlobalNavbar extends Component{
  constructor(props){
    super(props);
    this.state = { open: false };
  }


  handleToggle = () => this.setState({open: !this.state.open});

  handleClose = () => this.setState({open: false});

  render(){
  return(
    <nav className="global-nav">
    <div className="nav-wrapper">
          Global nav
      </div>
    </nav>
  );
}
}
