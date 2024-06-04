#!/usr/bin/env node
// read from file

const fs = require('fs');
const filename = process.argv[2];

if (filename === undefined) {
} else {
  fs.readFile(filename, 'utf8', function (err, data) {
    if (err) console.log(err);
    console.log(data);
  });
}
