#!/usr/bin/node
// Defines a Rectangle class

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      console.log([...Array(this.width).fill('X')].join(''));
    }
  }

  rotate() {
    [this.height, this.width] = [this.width, this.height]
  }

  double() {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;

