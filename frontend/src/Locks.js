import React, {Component} from "react";

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
  render() {
    const {locks, onPuzzleStateChanged} = this.props;
    return (
      <div>
        {locks.map(lock => <Lock {...lock} onPuzzleStateChanged={onPuzzleStateChanged}/>)}
      </div>
    )
  }
}

export default Locks;