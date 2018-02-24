import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import {locks, puzzles} from './api';
import LoadingError from './LoadingError';
import Loading from './Loading';
import Locks from './Locks';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      locks: [],
      error: false
    };
    this.changePuzzleState = this.changePuzzleState.bind(this);
  }

  loadData() {
    const self = this;
    locks.fetch().then((locks) => {
      self.setState({
        ...self.state,
        locks,
        loading: false,
        error: false
      })
    }).catch((err) => {
      console.log(err);
      self.setState({
        ...self.state,
        loading: false,
        error: true
      })
    });
  }

  componentDidMount() {
    this.loadData();
  }

  changePuzzleState(reporter, address, state) {
    const self = this;
    puzzles.set(reporter, address, state)
      .then(() => self.loadData());
  }

  render() {
    const {loading, locks, error} = this.state;
    const mainConent = loading
      ? <Loading/>
      : error
        ? <LoadingError/>
        : <Locks locks={locks} onPuzzleStateChanged={this.changePuzzleState}/>;

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo"/>
          <h1 className="App-title">Контрольная панель</h1>
        </header>
        <div className="App-content">
          {mainConent}
        </div>
      </div>
    );
  }
}

export default App;
