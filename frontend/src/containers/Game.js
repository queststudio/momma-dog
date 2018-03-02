import React, {Component} from "react";
import {games} from '../api/index';

class Game extends Component {
  constructor(props) {
    super(props);

    this.fetchData = this.fetchData.bind(this);
    this.restart = this.restart.bind(this);

    this.state = {};
  }

  componentDidMount() {
    this.fetchData()
  }

  fetchData() {
    const self = this;
    games.fetch()
      .then(game => self.setState({...self.state, game}));
  }

  restart() {
    const self = this;
    games.next().then(
        self.fetchData
    );
  }

  render() {
    const {game} = this.state;
    return (<div className="game-panel">
      <p>Игра {game || '...'}</p>
      <p className="restart-btn" onClick={this.restart}>Перезапустить</p>
    </div>);
  }
}

export default Game;