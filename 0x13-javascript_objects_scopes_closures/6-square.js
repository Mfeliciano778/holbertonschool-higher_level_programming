#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    let char = c;
    if (c === undefined || c === null) {
      char = 'X';
    }
    for (let row = 0; row < this.size; row++) {
      for (let column = 0; column < this.size; column++) {
        process.stdout.write(char);
      }
      console.log('');
    }
  }
}
module.exports = Square;
