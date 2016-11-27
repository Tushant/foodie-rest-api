import React,{Component} from 'react';
import { Link } from 'react-router';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { Card, Grid, Loader, Image } from 'semantic-ui-react';
import _ from 'lodash';

import Banner from './banner';
import Places from './places';
import Body from './body';
import FoodieForm from './foodie-form';
import { fetchRestaurant } from '../../actions/index';


class Content extends Component {
    componentDidMount(){
      this.props.fetchRestaurant();
    }

    render() {
        const { restaurant, fetching } = this.props;
        const restaura = _.map(restaurant.restaurants, (restaurant) => {
            return (
                    <Grid.Column
                        mobile={16} computer={5} tablet={8}
                        key={restaurant.id}
                        style={{ marginBottom: '20px' }}
                    >
                        <Card>
                            <Link to={"restaurant/" + restaurant.slug}>  {restaurant.image ?
                                              <Image src={restaurant.image} />
                                              :<Image src='http://semantic-ui.com/images/avatar2/large/matthew.png' />}
                            </Link>
                            <Card.Content>
                              <Card.Header>
                              <Link to={"restaurant/" + restaurant.slug}><span className="card-title">{restaurant.name}</span></Link>
                              </Card.Header>
                            </Card.Content>
                        </Card>
                    </Grid.Column>
            );
        });

        if (fetching) {
            return <Loader active inline='centered' />;
        }
        return (
                <div className="content">
                    <div className="masthead segment">
                        <Banner />
                        <Body />
                        <FoodieForm />
                   </div>
            <div className="ui container" style={{ marginTop: '100px' }}>
                <Places />
                <div className="ui attached stackable centered" style={{ marginTop: '100px' }}>
                    <div className="container">
                        <div>
                        {fetching}
                          <Grid verticalAlign='middle'>
                            <Grid.Row style={{ marginBottom: '20px' }}>
                                {restaura}
                            </Grid.Row>
                          </Grid>
                        </div>
                      </div>
                </div>
            </div>
            </div>
        );
    }
}

const mapStateToProps = (state) => ({
    restaurant: state.restaurantFetch
});

function mapDispatchToProps(dispatch) {
    return bindActionCreators({
        fetchRestaurant
    }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(Content);
