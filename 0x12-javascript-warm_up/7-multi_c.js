#!/usr/bin/node
const numOfTimes = process.argv[2];
if (!numOfTimes) {
  console.log('Missing number of occurrences');
}
for (let index = 0; index < numOfTimes; index++) {
  console.log('C is fun');
}
