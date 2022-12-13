#!/usr/bin/node
// Adds on to 5-square.js
const SQUARE = require('./5-square');

module.exports = class Square extends SQUARE {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
