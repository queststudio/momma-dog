import React, {Component} from "react";
import LoadingError from '../../LoadingError';
import Loading from '../../Loading';
import {switches} from '../../api/index';

class State extends Component {
  render() {
    const {state} = this.props;
    const stateMap = {
      on: 'вкл',
      off: 'выкл'
    };
    return <p>{stateMap[state]}</p>;
  }
}

class Switch extends Component {
  render() {
    const {id, label, state, changeState} = this.props;
    const toggled = state === 'on' ? 'off' : 'on';
    const onStateChanged = () => changeState(id, toggled);
    const stateClass = state === 'on' ? 'switch-on' : 'switch-off';
    const className = ['switch', stateClass].join(' ');
    return (
      <div className={className} onClick={onStateChanged}>
        <p>{label}</p>
        <State state={state}/>
      </div>
    );
  }
}

class Switches extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      switches: [],
      error: false
    };
    this.changeSwitchState = this.changeSwitchState.bind(this);
    this.loadData = this.loadData.bind(this);
  }

  loadData() {
    const self = this;
    switches.fetch().then((switches) => {
      self.setState({
        ...self.state,
        switches,
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
    setInterval(this.loadData, 2000);
  }

  changeSwitchState(id, state) {
    const self = this;
    switches.set(id, state)
      .then(() => self.loadData());
  }

  render() {
    const {loading, switches, error} = this.state;
    const main = loading
      ? <Loading/>
      : error
        ? <LoadingError/>
        : switches.map(lock => <Switch {...lock} changeState={this.changeSwitchState}/>);

    return (
      <div className="switches">
        <p>Выключатели</p>
        {main}
      </div>
    )
  }
}

export default Switches;