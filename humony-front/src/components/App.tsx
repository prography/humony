import React, { Component, Suspense, lazy } from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import '../styles/reset.scss';

const MainPage = lazy(() => import('../pages/MainPage'));
const Intro = lazy(() => import('../pages/IntroPage'));

class App extends Component {
  render() {
    return (
      <div className="App">
        <BrowserRouter>
          <Suspense fallback={<div>Loading...</div>}>
              <Switch>
                  <Route exact path="/" component={MainPage} />
                  <Route exact path="/intro" component={Intro} />
              </Switch>
          </Suspense>
        </BrowserRouter>
      </div>
    );
  }
};

export default App;
