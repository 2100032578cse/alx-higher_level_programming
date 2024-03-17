#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const ch = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(ch.repeat(this.width));
    }
  }
};
