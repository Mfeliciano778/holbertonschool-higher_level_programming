#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      for (let column = 0; column < this.width; column++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }

  rotate () {
    if (this.height > 0 && this.width > 0) {
      this.width = this.height;
      this.height = this.width;
    }
  }

  double () {
    if (this.height > 0 && this.width > 0) {
      this.width = this.width * 2;
      this.height = this.height * 2;
    }
  }
}
module.exports = Rectangle;
