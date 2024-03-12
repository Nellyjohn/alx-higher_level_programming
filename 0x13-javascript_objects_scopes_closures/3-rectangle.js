#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w >= 0 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    let x = 0;
    let y = 0;
    while (x < this.height) {
      while (y < this.width) {
        str += 'X';
        y++;
      }
      console.log(str);
      x++;
    }
  }
};
