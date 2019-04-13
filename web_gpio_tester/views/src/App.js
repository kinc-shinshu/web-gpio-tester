import React, { Component } from 'react';
import 'bulma';

class Controller extends Component {
  gpioOn = async () => {
    const pinNumber = this.props.pinNumber;
    const uri = `http://127.0.0.1:5000/gpio/${pinNumber}/out`
    const result = await fetch(uri, {
        method: "POST",
        body: JSON.stringify({value: 1}),
        headers: {
          "Content-Type": "application/json"
        }
      }).then(response => response.json());
    console.log(result);
  };

  gpioOff = async () => {
    const pinNumber = this.props.pinNumber;
    const uri = `http://127.0.0.1:5000/gpio/${pinNumber}/out`
    const result = await fetch(uri, {
        method: "POST",
        body: JSON.stringify({value: 0}),
        headers: {
          "Content-Type": "application/json"
        }
      }).then(response => response.json());
    console.log(result);
  };

  render() {
    return (
      <section className="hero is-light">
        <div className="hero-body">
          <h1 className="title">GPIO {this.props.pinNumber}</h1>
          <button className="button" onClick={this.gpioOn}>ON</button>
          <button className="button" onClick={this.gpioOFF}>OFF</button>
        </div>
      </section>
    );
  }
}

class App extends Component {

  render() {
    return (
      <div className="App">
        <div className="container">
          <Controller pinNumber="21" />
        </div>
      </div>
    );
  }
}

export default App;
