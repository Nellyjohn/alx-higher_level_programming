#!/usr/bin/node

exports.logMe = function (item) {
  if (this.key === undefined) {
    this.key = 0;
  }
  console.log(`${this.key}: ${item}`);
  this.key++;
};
