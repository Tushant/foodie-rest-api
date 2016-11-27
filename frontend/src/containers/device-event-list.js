import React, {Component, PropTypes} from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import _ from 'lodash';

import { selectDeviceEvent, CancelDeviceEvent } from '../actions/index';

class CreateADevice extends Component {
  constructor(props) {
    super(props);
    console.log(props);
  }

  // handleClick(event){
  //   const device_event_id = event.target.id;
  //   console.log('id',device_event_id);
  //   this.props.onClick(device_event_id);
  // }

  renderDeviceEventList(){
    return _.map(this.props.deviceEventOptions, (device_event_option) => {
      return (
              <i key={device_event_option.id}
              id={device_event_option.id}
              className={device_event_option.class}
              onClick={() => this.props.selectDeviceEvent(device_event_option)}>
              {device_event_option.icon_name}
              </i>
            );
    });
  }
  render() {
    return (
        <div>
          {this.renderDeviceEventList()}
        </div>
      );
  }
}


function mapStateToProps(state){
   // whatever is returned will show up as props
   // inside of DeviceEventList Component
   return{
    // asdf:'123'
    // this.props.deviceEventOptions will have value 'icon_name, class, id,open' from state 
    //that is in reducer as deviceEventOptions key with value 'icon_name,class,id,open'
    deviceEventOptions:state.deviceEventOption
   };
}

function mapDispatchToProps(dispatch){
  // dispatching action named selectForm is passed to all reducers with the same key name which will be used as props
  // in the container for triggering selectForm action

  return bindActionCreators({ selectDeviceEvent: selectDeviceEvent, CancelDeviceEvent: CancelDeviceEvent }, dispatch);
}

export default connect (mapStateToProps, mapDispatchToProps)(CreateADevice);
