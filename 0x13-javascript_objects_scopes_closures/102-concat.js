#!/usr/bin/node
// Concatenates two files.
const fs = require('fs');

function generateFile (fileA, fileB, result) {
  let file = '';
  file = fs.readFileSync(fileA, 'utf8');
  file += fs.readFileSync(fileB, 'utf8');
  fs.writeFileSync(result, file);
}

generateFile(process.argv[2], process.argv[3], process.argv[4]);
