import React, { Component } from 'react';
import _ from 'lodash';
import Masonry from 'react-masonry-component';
import { connect } from 'react-redux';

const masonryOptions = {
    transitionDuration: '0.8s',
    columnWidth: 400,
    gutter: 30,
    isFitWidth: true
};

class Places extends Component {
	render() {
		const style = { marginTop: 10, width: 400 };
		const { placesReducer } = this.props;
		const childElements = _.map(placesReducer, (place) =>
			<div className="placesPhoto" key={place.id}>
        <img
          key={place.id}
          src={place.image}
          alt={place.place}
          style={style}
          className="img-responsive"
		      />
        <p>{place.place}</p>
      </div>
	    );
		return (
			<div className="places">
        <div className="placeHeading">
          <h2>Most Popular Places</h2>
          <Masonry
            elementType={'div'}
            className='my-gallery-class'
            options={masonryOptions}
          >
            {childElements}
          </Masonry>
        </div>
      </div>
			);
	}
}

const mapStateToProps = (state) => ({
    placesReducer: state.placesReducer
});

export default connect(mapStateToProps, null)(Places);
