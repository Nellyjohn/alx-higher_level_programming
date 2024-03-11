#!/usr/bin/node
const myMessage1 = 'No argument';
const myMessage2 = 'Argument found';
const myMessage3 = 'Arguments found';

if (process.argv.length === 2) {
  console.log(myMessage1);
} else if (process.argv.length === 3) {
  console.log(myMessage2);
} else {
  console.log(myMessage3);
}
