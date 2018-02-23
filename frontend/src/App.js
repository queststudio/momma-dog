import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';

class Puzzle extends Component {
  render() {
    const {label, state} = this.props;
    return (
      <div>
        <p>{label}</p>
        <p>
          {state}
        </p>
      </div>
    );
  }
}

class Lock extends Component {
  render() {
    const {label, state, puzzles, onPuzzleStateChanged} = this.props;
    return (
      <div>
        <p>{label}</p>
        <p>{state}</p>
        <div>
          {puzzles.map(puzzle => <Puzzle {...puzzle} onStateChanged={onPuzzleStateChanged}/>)}
        </div>
      </div>
    );
  }
}

class Locks extends Component {
  render() {
    const {locks} = this.props;
    return (
      <div>
        {locks.map(lock => <Lock {...lock}/>)}
      </div>
    )
  }
}

class Loading extends Component {
  render() {
    return (
      <p>
        Подгружаю данные...
      </p>
    );
  }
}

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      locks: []
    };
  }

  puzzleStateChanged(reporter, address) {
    console.log(`[${reporter}:${address}] clicked`);
  }

  fetchLocks() {
    const locks = {"locks": [{"label": "ira", "state": "closed", "puzzles": [{"reporter": "62:01:94:70:60:70", "local_address": 8, "state": "unknown"}], "address": 56, "port": 0}, {"label": "\u0442\u0435\u043c\u043d\u0430\u044f \u043a\u043e\u043c\u043d\u0430\u0442\u0430", "state": "closed", "puzzles": [{"reporter": "62:01:94:70:60:70", "local_address": 9, "state": "unknown"}], "address": 56, "port": 1}, {"label": "\u0442\u0435\u043c\u043d\u0430\u044f \u043a\u043e\u043c\u043d\u0430\u0442\u0430 - \u0441\u0432\u0435\u0442", "state": "closed", "puzzles": [{"reporter": "62:01:94:70:60:70", "local_address": 10, "state": "unknown"}], "address": 56, "port": 2}, {"label": "acedia", "state": "closed", "puzzles": [{"reporter": "62:01:94:70:60:70", "local_address": 11, "state": "unknown"}], "address": 56, "port": 3}, {"label": "superbia - \u0441\u0432\u0435\u0442", "state": "closed", "puzzles": [{"reporter": "62:01:94:70:60:70", "local_address": 12, "state": "unknown"}], "address": 56, "port": 4}, {"label": "superbia - \u043a\u043e\u0434", "state": "closed", "puzzles": [{"reporter": "62:01:94:70:60:70", "local_address": 13, "state": "unknown"}], "address": 56, "port": 5}, {"label": "avarice", "state": "closed", "puzzles": [{"reporter": "62:01:94:70:60:70", "local_address": 14, "state": "unknown"}], "address": 56, "port": 6}, {"label": "\u0441\u0443\u043d\u0434\u0443\u043a - 1", "state": "closed", "puzzles": [{"reporter": "62:01:94:70:60:70", "local_address": 15, "state": "unknown"}], "address": 56, "port": 7}]};
    return Promise.resolve(locks);
  }

  componentDidMount() {
    this.fetchLocks().then((result) => {
      this.setState({
        locks: result.locks,
        loading: false
      })
    })
  }

  render() {
    const {loading, locks} = this.state;
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo"/>
          <h1 className="App-title">Контрольная панель</h1>
        </header>
        {loading
          ? <Loading/>
          : <Locks locks={locks} onPuzzleStateChanged={this.puzzleStateChanged}/>
        }
      </div>
    );
  }
}

export default App;
