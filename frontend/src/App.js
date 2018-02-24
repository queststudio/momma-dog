import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import Locks from './containers/Locks';
import Switches from './containers/Switches';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo"/>
          <h1 className="App-title">Контрольная панель</h1>
        </header>
        <div className="App-content">
          <Locks/>
          <br/>
          <Switches/>
        </div>
      </div>
    );
  }
}

export default App;
