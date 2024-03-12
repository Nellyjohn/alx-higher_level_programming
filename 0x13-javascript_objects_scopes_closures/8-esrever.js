#!/usr/bin/node

exports.esrever = function (list) {
  const myArray = [];
  let listIndex = list.length - 1;
  while (listIndex >= 0) {
    myArray.push(list[listIndex]);
    listIndex--;
  }
  return myArray;
};
