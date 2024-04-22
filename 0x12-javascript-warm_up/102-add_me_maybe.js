#!/usr/bin/node

module.exports = {
  addMeMaybe: function (n, func) {
    return func(n + 1);
  }
};
