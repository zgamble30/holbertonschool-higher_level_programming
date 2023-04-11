#!/usr/bin/node
// Class Rectangle that defines a rectangle
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const w = parseInt(this.width);
    const h = parseInt(this.height);

    for (let i = 0; i < h; i++) {
      console.log('X'.repeat(w));
    }
  }
}

module.exports = Rectangle;
