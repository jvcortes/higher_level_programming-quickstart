#!/usr/bin/node
// Defines a Square class
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint(c) {
    for (let i = 0; i < this.height; i++) {
      console.log([...Array(this.width).fill(c ? c : 'X')].join(''));
    }
  }
}

module.exports = Square;
