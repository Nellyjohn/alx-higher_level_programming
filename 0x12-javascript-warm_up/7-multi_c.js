#!/usr/bin/node
const x = process.argv[2];
const num = parseInt(x);
let count = 0;

if (!num) {
  console.log('Missing number of occurrences');
} else {
  while (count < x) {
    console.log('C is fun');
    count++;
  }
}
