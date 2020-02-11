#!/usr/bin/node
// Defines a Square class
const Square_ = require('./5-square');

class Square extends Square_ {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      console.log([...Array(this.width).fill(c || 'X')].join(''));
    }
  }
}

module.exports = Square;
