#!/usr/bin/node
const myArg = process.argv[2];
const num = parseInt(myArg);
let count = 0;

if (!num) {
  console.log('Missing size');
} else {
  while (count < myArg) {
    console.log('X'.repeat(num));
    count++;
  }
}
