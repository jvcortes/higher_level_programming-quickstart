#!/usr/bin/node
// Writes to a file,
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], function (err, content) {
  if (err) {
    console.log(err);
  }
});
