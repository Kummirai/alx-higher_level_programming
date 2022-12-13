#!/usr/bin/node
// Class Square that inherits from class Rectangle in 4-rectangle.js
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
