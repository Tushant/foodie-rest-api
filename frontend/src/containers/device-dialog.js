import React, {Component, PropTypes} from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import {Button, Dialog, DialogTitle, DialogContent, DialogActions,
        Textfield} from 'react-mdl';

import { CancelDeviceEvent } from '../actions/index';


class DeviceDialog extends Component {
  constructor(props) {
    super(props);
    console.log('this.props',this.props.onChange);
  }

  handleInputChange(event){
    let name = event.target.value;
    this.props.onChange(name);
  }

  renderOwnADevice(){
    console.log('open',this.props.active_device_event.open);
    return(
      <div className="device-action">
        <Dialog open={this.props.active_device_event.open} onCancel={this.props.CancelDeviceEvent}>
          <DialogTitle>Own a Device</DialogTitle>
          <DialogContent>
              <Textfield
                  onChange={(event)=> {this.handleInputChange(event)}}
                  pattern="-?[0-9]*(\.[0-9]+)?"
                  error="Input is not a number!"
                  label="Device Serial Number"
                  floatingLabel
                />
                <span style={{ float:'right'}}>{this.props.remaningChar}/32</span>
          </DialogContent>
          <DialogActions>
            <Button type='button' onClick={this.props.CancelDeviceEvent}>Cancel</Button>
            <Button type='button'>Own</Button>
          </DialogActions>
        </Dialog>
      </div>
    )
  }

  renderFollowADevice(){
    return(
      <div className="device-action">
        <Dialog open={this.props.active_device_event.open} onCancel={this.props.CancelDeviceEvent}>
          <DialogTitle>Follow a Device</DialogTitle>
          <DialogContent>
            <Textfield
                onChange={(event) => this.props.onChange(event)}
                pattern="-?[0-9]*(\.[0-9]+)?"
                error="Input is not a number!"
                label="Device Serial Number"
                floatingLabel
              />
              <span style={{ float:'right'}}>{this.props.remaningChar}/32</span>
          </DialogContent>
          <DialogActions>
            <Button type='button' onClick={this.props.CancelDeviceEvent}>Cancel</Button>
            <Button type='button'>Follow</Button>
          </DialogActions>
        </Dialog>
      </div>
    )
  }

  render() {
    // const device_event_type = this.props.active_device_event.icon_name;
    console.log('device_event_type',this.props.CancelDeviceEvent);
    if ( !this.props.active_device_event){
      return <h5 style={{ textAlign:'center' }}>Click icon based on your work</h5>;
    }

    let icon_name = this.props.active_device_event.icon_name;

    if( icon_name == 'devices_other'){
      return (<div>Device Other</div>);
    }
    if( icon_name == 'device_hub'){
      return (<div>Device Hub</div>);
    }
    if( icon_name == 'add_circle_outline'){
      return (this.renderOwnADevice());
    }
    if( icon_name == 'remove_red_eye'){
      return (this.renderFollowADevice());
    }
    if( icon_name == 'share'){
      return (<div>Share</div>);
    }
    if( icon_name == 'edit'){
      return (<div>Edit</div>);
    }
    if( icon_name == 'trending_up'){
      return (<div>Trending up</div>);
    }
  }
}

function mapStateToProps(state){
  // state is defined in reducers. In my case i have defined this state in reducers-active-device-event.js
  return{
    active_device_event: state.activeDeviceEvent
  };
}

function mapDispatchToProps(dispatch){
  // dispatching action named CancelDeviceEvent is passed to all reducers with the same key name which will be used as props
  // in the container for triggering CancelDeviceEvent action

  return bindActionCreators({ CancelDeviceEvent: CancelDeviceEvent }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(DeviceDialog);
