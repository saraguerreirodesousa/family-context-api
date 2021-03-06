import React from "react";

import thunkMiddleware from "redux-thunk";
import { createLogger } from "redux-logger";
import { createStore, applyMiddleware } from "redux";
import { Provider } from "react-redux";

import {createMuiTheme} from "@material-ui/core/styles";
import { ThemeProvider } from '@material-ui/styles';

import rootReducer from "./reducers";
import Auth from "./components/authentication/auth";
import Router from "./Router"

const loggerMiddleware = createLogger();

const store = createStore(
    rootReducer,
    applyMiddleware(
        thunkMiddleware, // lets us dispatch() functions
        loggerMiddleware // neat middleware that logs actions
    )
);

const theme = createMuiTheme({
    palette: {
        primary: {
            main: '#00675b',
        },
    },
});

function App() {
  return (
      <Provider store={store}>
          <ThemeProvider theme={theme}>
              <Auth>
                  <Router />
              </Auth>
          </ThemeProvider>
      </Provider>
  );
}

export default App;
