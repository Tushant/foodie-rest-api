import React, {Component} from 'react';
import _ from 'lodash';
import { Grid } from 'semantic-ui-react';

const PersonalInfo = ({restaurant}) => {
  const feature = _.map(restaurant.features, (feature) => {
       return _.join(feature.features, ',');
  });
  const timing = _.map(restaurant.timings, (timing) => {
    return _.join(timing.timings, ',');
  })
  return(
      <div style={{ marginTop:'20px' }}>
        <Grid>
          <Grid.Row>
            <Grid.Column mobile={16} computer={5} tablet={8}>
              <p className="flow-text attribute">Name</p>
              <span>{restaurant.name}</span>
            </Grid.Column>
            <Grid.Column xs={12} sm={12} md={4} >
              <p className="flow-text attribute">Owner</p>
              <span>{restaurant.owner}</span>
            </Grid.Column>
            <Grid.Column xs={12} sm={12} md={4} >
              <p className="flow-text attribute">Address</p>
              <span>{restaurant.address}</span>
            </Grid.Column>
          </Grid.Row>
          <Grid.Row>
            <Grid.Column xs={12} sm={12} md={4} >
              <p className="flow-text attribute">Features</p>
              <span>{feature}</span>
            </Grid.Column>
            <Grid.Column xs={12} sm={12} md={4} >
              <p className="flow-text attribute">Phone Number</p>
              <span>{restaurant.phone_number}</span>
            </Grid.Column>
            <Grid.Column xs={12} sm={12} md={4} >
              <p className="flow-text attribute">Owner Email</p>
              <span>{restaurant.owner_email}</span>
            </Grid.Column>
          </Grid.Row>
          <Grid.Row>
            <Grid.Column xs={12} sm={12} md={4} >
              <p className="flow-text attribute">City</p>
              <span>{restaurant.city}</span>
            </Grid.Column>
            <Grid.Column xs={12} sm={12} md={4} >
              <p className="flow-text attribute">Wifi</p>
              <span>{restaurant.is_wifi ? 'Yes' : 'No'}</span>
            </Grid.Column>
            <Grid.Column xs={12} sm={12} md={4} >
              <p className="flow-text attribute">Parking</p>
              <span>{restaurant.is_parking ? 'Yes' : 'No'}</span>
            </Grid.Column>
          </Grid.Row>
          <Grid.Row>
            <Grid.Column xs={12} sm={12} md={4} >
              <p className="flow-text attribute">Website</p>
              <span>{restaurant.website ? restaurant.website : 'sorry' }</span>
            </Grid.Column>
            <Grid.Column xs={12} sm={12} md={4} >
              <p className="flow-text attribute">Facebook</p>
              <span>{restaurant.facebook}</span>
            </Grid.Column>
            <Grid.Column xs={12} sm={12} md={4} >
              <p className="flow-text attribute">Twitter</p>
              <span>{restaurant.twitter}</span>
            </Grid.Column>
          </Grid.Row>
        </Grid>
        <Grid>
          <Grid.Column xs={12} sm={12} md={4} >
            <p className="flow-text attribute">Description</p>
            <span>{restaurant.other_detail ? restaurant.other_detail : 'he is too busy'}</span>
          </Grid.Column>
          <Grid.Column xs={12} sm={12} md={4} >
            <p className="flow-text attribute">Timings</p>
            <span>{timing}</span>
          </Grid.Column>
        </Grid>
      </div>
  )
}

export default PersonalInfo;
