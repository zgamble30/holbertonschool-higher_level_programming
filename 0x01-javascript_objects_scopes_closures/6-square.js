#!/usr/bin/node
// Class Square that defines a square and inherits from Square of 5-square.js

const superSquare = require('./5-square');

class Square extends superSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let j = 0; j < this.width; j++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
