#!/usr/bin/node
const arg1 = process.argv[2];
if (arg1 === undefined) {
  console.log('No argument');
}
console.log(arg1);
