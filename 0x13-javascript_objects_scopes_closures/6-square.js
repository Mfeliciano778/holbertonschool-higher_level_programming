#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined || c === null) {
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
