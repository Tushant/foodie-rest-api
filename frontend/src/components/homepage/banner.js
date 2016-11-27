import React from 'react';
import { Link } from 'react-router';

const Banner = (props) => (
   <div className="navbar-container">
        <div className="ui container">
            <div className="ui large secondary menu">
                <a className="toc item">
                    <i className="sidebar icon"></i>
                </a>
                <div className="item logo">
                    <div className="ui logo shape">
                        <div className="sides">
                            <div className="active ui side">
                                Foodie
                            </div>
                        </div>
                    </div>
                </div>
                <Link to="/restaurant" className="active item tab">Home</Link>
                <Link to='/addrestaurant' className='item tab'>Add Restaurant</Link>
                <Link to="/products" className="item tab">Products</Link>
                <div className="right item">
                    <a href="" id="bookingInfoButton" className="ui white inverted button">Booking</a>
                </div>
            </div>
        </div>
      </div>
);

export default Banner;
