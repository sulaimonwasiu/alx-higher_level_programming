#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    let str = c.repeat(this.size) + '\n';
    str = str.repeat(this.size);
    console.log(str);
  }
}

module.exports = Square;
