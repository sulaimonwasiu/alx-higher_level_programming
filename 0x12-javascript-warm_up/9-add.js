#!/usr/bin/node
const args = process.argv;
const arg1 = parseInt(args[2]);
const arg2 = parseInt(args[3]);

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  return a + b;
}
console.log(add(arg1, arg2));
