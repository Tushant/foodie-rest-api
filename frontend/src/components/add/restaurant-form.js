import React from 'react';
import { Field, reduxForm, formValueSelector } from 'redux-form';
import { connect } from 'react-redux';
import {
        Grid,
        Button,
        Checkbox,
        Form,
        Message,
        List
     } from 'semantic-ui-react';

 const validate = values => {
  const errors = {};
  const requiredFields = ['restaurantName', 'address', 'ownerEmail'];
  requiredFields.forEach(field => {
    if (!values[field]) {
      errors[field] = 'Required';
    }
});
  return errors;
};

 const renderTextField = ({ input, label, type, meta: { touched, error } }) => (
    <div>
     <Form.Input label={label} type={type} {...input} />
     <span style={{ color: 'red' }}>{touched && error}</span>
    </div>
 );


 const RestaurantForm = (props) => {
   const { handleSubmit } = props;
   return (
     <Grid>
        <Grid.Row>
            <Grid.Column mobile={12} computer={12} tablet={12}>
                <form onSubmit={handleSubmit} className="ui segment form">
                  <div className="form-field">
                    <label>RESTAURANT NAME*</label>
                    <div>
                      <Field name="restaurantName" component={renderTextField} type='text' />
                    </div>
                  </div>
                  <div className="form-field">
                    <label>ADDRESS*</label>
                      <Field name="address" component={renderTextField} type='text' />
                  </div>
                  <div className="form-field">
                    <label>RESTAURANT EMAIL</label>
                      <Field name="ownerEmail"component={renderTextField} type='email' />
                  </div>
                  <div className="form-field">
                    <label>RESTAURANT PHONE NUMBER</label>
                      <Field name="phoneNumber" component={renderTextField} type='number' />
                  </div>
                  <div className="form-field">
                    <label>RESTAURANT WEBSITE</label>
                      <Field name="website" component={renderTextField} type='text' />
                  </div>
                  <div className="form-field">
                      <label>FACEBOOK PAGE</label>
                      <Field name="facebookPage" component={renderTextField} type='text' />
                  </div>
                  <div className="form-field">
                    <label>TWITTER HANDLE</label>
                      <Field name="twitterHandle" component={renderTextField} type='text' />
                  </div>
                  <div className="form-field">
                    <label>OTHER DETAILS</label>
                      <Field name="otherDetail" component={renderTextField} type='text' />
                  </div>
                    <Button type="submit">Submit</Button>
                </form>
            </Grid.Column>
            <Grid.Column mobile={12} computer={4} tablet={4}>
              <div className="ui segment" style={{ marginTop: '40px' }}>
                <div className="Notice">
                  Check your detail before submitting
                </div>
                <div className="detail" style={{ marginTop: '20px' }}>
                { props.restaurantName ? 
                    <List divided relaxed>
                      <List.Item>
                        <List.Content>
                          <List.Header as='a'>Restaurant Name</List.Header>
                          <List.Description as='a'>{props.restaurantName}</List.Description>
                        </List.Content>
                      </List.Item>
                    </List> :
                    '' 
                }
                { props.address ? 
                    <List divided relaxed>
                      <List.Item>
                        <List.Content>
                          <List.Header as='a'>Address</List.Header>
                          <List.Description as='a'>{props.address}</List.Description>
                        </List.Content>
                      </List.Item>
                    </List> :
                    '' 
                }
                { props.ownerEmail ? 
                    <List divided relaxed>
                      <List.Item>
                        <List.Content>
                          <List.Header as='a'>Owner Email</List.Header>
                          <List.Description as='a'>{props.ownerEmail}</List.Description>
                        </List.Content>
                      </List.Item>
                    </List> :
                    '' 
                }
                { props.phoneNumber ? 
                    <List divided relaxed>
                      <List.Item>
                        <List.Content>
                          <List.Header as='a'>Phone Number</List.Header>
                          <List.Description as='a'>{props.phoneNumber}</List.Description>
                        </List.Content>
                      </List.Item>
                    </List> :
                    '' 
                }
                { props.website ? 
                    <List divided relaxed>
                      <List.Item>
                        <List.Content>
                          <List.Header as='a'>Website</List.Header>
                          <List.Description as='a'>{props.website}</List.Description>
                        </List.Content>
                      </List.Item>
                    </List> :
                    '' 
                }
                { props.facebookPage ? 
                    <List divided relaxed>
                      <List.Item>
                        <List.Content>
                          <List.Header as='a'>Facebook Page</List.Header>
                          <List.Description as='a'>{props.facebookPage}</List.Description>
                        </List.Content>
                      </List.Item>
                    </List> :
                    '' 
                }
                { props.twitterHandle ? 
                    <List divided relaxed>
                      <List.Item>
                        <List.Content>
                          <List.Header as='a'>Twitter Handle</List.Header>
                          <List.Description as='a'>{props.twitterHandle}</List.Description>
                        </List.Content>
                      </List.Item>
                    </List> : 
                    '' 
                }
                { props.otherDetail ? 
                    <List divided relaxed>
                      <List.Item>
                        <List.Content>
                          <List.Header as='a'>Other Detail</List.Header>
                          <List.Description as='a'>{props.otherDetail}</List.Description>
                        </List.Content>
                      </List.Item>
                    </List> : 
                    '' 
                }
                </div>
              </div>
            </Grid.Column>
        </Grid.Row>
    </Grid>
   )
 }

 const selector = formValueSelector('addRestaurant');

const mapStateToProps = state => {
    const restaurantName = selector(state, 'restaurantName');
    const address = selector(state, 'address');
    const ownerEmail = selector(state, 'ownerEmail');
    return {
        restaurantName,
        address,
        ownerEmail
    };
  };

 const AddRestaurantForm = reduxForm({
   form: 'addRestaurant',
   validate,
  destroyOnUnmount: false,
})(RestaurantForm);

export default connect(mapStateToProps, null)(AddRestaurantForm);