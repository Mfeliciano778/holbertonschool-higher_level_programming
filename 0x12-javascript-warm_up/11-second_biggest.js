#!/usr/bin/node
const leng = process.argv.length;
let bigInt = 0;
let secBig = 0;
if (leng > 3) {
  for (let index = 0; index < process.argv.length; index++) {
    if (parseInt(process.argv[index]) > bigInt) {
      bigInt = process.argv[index];
    }
  }
  for (let index = 0; index < process.argv.length; index++) {
    if (parseInt(process.argv[index]) < bigInt &&
        parseInt(process.argv[index]) > secBig) {
      secBig = process.argv[index];
    }
  }
  console.log(secBig);
} else {
  console.log(0);
}
