#!/usr/bin/node
const myConcatenator = ' is ';
if (process.argv.length === 4) {
  console.log(process.argv[2] + myConcatenator + process.argv[3]);
} else if (process.argv.length === 3) {
  console.log(process.argv[2] + myConcatenator + undefined);
} else {
  console.log(undefined + myConcatenator + undefined);
}
