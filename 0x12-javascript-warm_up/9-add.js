#!/usr/bin/node
const firstInteger = parseInt(process.argv[2]);
const secondInteger = parseInt(process.argv[3]);
function add (a, b) {
  const result = a + b;
  console.log(result);
}

add(firstInteger, secondInteger);
