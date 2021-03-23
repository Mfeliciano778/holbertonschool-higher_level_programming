#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let row = 0; row < this.size; row++) {
        for (let column = 0; column < this.size; column++) {
          process.stdout.write('C');
        }
        console.log('');
      }
    }
  }
}
module.exports = Square;
