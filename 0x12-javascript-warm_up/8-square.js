#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
}
const size = process.argv[2];
for (let row = 0; row < size; row++) {
  for (let column = 0; column < size; column++) {
    process.stdout.write('X');
  }
  console.log('');
}
