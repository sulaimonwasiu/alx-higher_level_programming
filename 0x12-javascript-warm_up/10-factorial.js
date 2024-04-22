#!/usr/bin/node

const argument = process.argv[2];
const n = parseInt(argument);

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(n));
