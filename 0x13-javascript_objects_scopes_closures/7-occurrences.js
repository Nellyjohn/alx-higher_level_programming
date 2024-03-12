#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let listIndex = 0;
  let count = 0;
  while (listIndex < list.length) {
    if (list[listIndex] === searchElement) {
      count += 1;
    }
    listIndex++;
  }
  return count;
};
