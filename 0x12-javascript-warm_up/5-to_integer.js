#!/usr/bin/node
const str = process.argv[2];
const num = parseInt(str);
if (!num) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
