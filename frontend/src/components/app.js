import React, { Component, PropTypes } from 'react';
import HomeScreen from './homepage/homescreen';

class App extends Component {
  constructor(props){
    super(props);
    this.state = { loading: false, display: false };
}

  handleDrawer = () => {
      this.setState({
          display: !this.state.display
      });
  }

  render() {
    return (
         <HomeScreen
            handleDrawer={this.handleDrawer}
            display={this.state.display}
        />
    );
  }
}

export default App;
