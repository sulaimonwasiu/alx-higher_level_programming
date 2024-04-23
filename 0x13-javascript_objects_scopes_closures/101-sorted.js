#!/usr/bin/node

const { dict } = require('./101-data.js');

const newDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];

  if (!(occurrences in newDict)) {
    newDict[occurrences] = [];
  }

  newDict[occurrences].push(userId);
}

const sortedKeys = Object.keys(newDict).sort((a, b) => a - b);
const sortedDict = {};

for (const key of sortedKeys) {
  sortedDict[key] = newDict[key];
}

console.log(sortedDict);
