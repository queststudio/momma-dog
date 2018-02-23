import React, {Component} from "react";

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

export default Locks;