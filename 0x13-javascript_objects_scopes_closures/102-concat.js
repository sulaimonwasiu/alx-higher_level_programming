#!/usr/bin/node

const fs = require('fs');

function concatFiles (source1, source2, destination) {
  const file1Content = fs.readFileSync(source1, 'utf8');
  const file2Content = fs.readFileSync(source2, 'utf8');
  const concatenatedContent = file1Content + file2Content;

  fs.writeFileSync(destination, concatenatedContent);
}

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

concatFiles(sourceFile1, sourceFile2, destinationFile);
