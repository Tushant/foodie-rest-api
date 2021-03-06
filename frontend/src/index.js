import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';

import App from './components/app';
import reducers from './reducers';

const createStoreWithMiddleware = applyMiddleware(thunk)(createStore);

  window.app = {
      showHomePage: function(id,data){
          render(
            <Provider store={createStoreWithMiddleware(reducers)}>
                <App />
            </Provider>, document.querySelector(id)
          );
      },
}
