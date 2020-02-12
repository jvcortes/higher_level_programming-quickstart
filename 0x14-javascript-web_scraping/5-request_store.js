#!/usr/bin/node
// Copies a HTTP GET response body to a file.
const request = require('request');
const fs = require('fs');

request(process.argv[2],
  function (err, response, body) {
    if (err) {
      console.error(err);
    } else {
      fs.writeFileSync(process.argv[3], body, 'utf8');
    }
  }
);
