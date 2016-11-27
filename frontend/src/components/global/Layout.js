import React, {Component, PropTypes} from 'react';
import GlobalNavbar from './GlobalNavbar';


export default class Layout extends Component {

  render(){
  return(
    <div className="container-fluid" style={{ paddingLeft:'0', paddingRight:'0' }}>
      <GlobalNavbar />
      {this.props.children}
    </div>
  )
}
}
