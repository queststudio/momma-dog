import React, {Component} from "react";
import LoadingError from '../../LoadingError';
import Loading from '../../Loading';
import {locks, puzzles} from '../../api/index';

class State extends Component {
  render(){
    const {state} = this.props;
    const stateMap = {
      unknown:'не найден',
      solved: 'решен',
      unsolved: 'не решен'
    };
    return <p>{stateMap[state]}</p>
  }
}

class Puzzle extends Component {
  render() {
    const {reporter, local_address, state, onStateChanged} = this.props;
    const solvedClass = state === 'solved' ? 'solved': 'not-solved';
    const className = ['puzzle', solvedClass].join(' ');
    return (
      <div className={className} onClick={()=>onStateChanged(reporter, local_address, 'solved')}>
        <p>{reporter}</p>
        <p>{local_address}</p>
        <State state={state}/>
      </div>
    );
  }
}

class Lock extends Component {
  render() {
    const {label, state, puzzles, onPuzzleStateChanged} = this.props;
    return (
      <div className='lock'>
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
    const main = loading
      ? <Loading/>
      : error
        ? <LoadingError/>
        : locks.map(lock => <Lock {...lock} onPuzzleStateChanged={this.changePuzzleState}/>);

    return (
      <div className="locks">
        <p>Замки</p>
        {main}
      </div>
    )
  }
}

export default Locks;