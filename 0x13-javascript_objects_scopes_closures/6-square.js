#!/usr/bin/node

const Square2 = require('./5-square.js');
module.exports = class Square extends Square2 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let x = 0;
    let y = 0;
    let str = '';
    while (x < this.height) {
      while (y < this.width) {
        str += c;
        y++;
      }
      console.log(str);
      x++;
    }
  }
};
