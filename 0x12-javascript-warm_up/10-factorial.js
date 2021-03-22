#!/usr/bin/node
const num = process.argv[2];
function numFact (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num === 1) {
    return 1;
  } else {
    return (num * numFact(num - 1));
  }
}
console.log(numFact(num));
