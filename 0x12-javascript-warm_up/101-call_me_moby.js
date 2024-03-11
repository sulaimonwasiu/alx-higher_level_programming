#!/usr/bin/node

function executeXTimes (x, func) {
  for (let i = 0; i < x; i++) {
    func();
  }
}

module.exports = executeXTimes;
