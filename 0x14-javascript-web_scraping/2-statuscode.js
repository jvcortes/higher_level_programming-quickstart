#!/usr/bin/node
// Makes a HTTP request and displays its status code.
const request = require('request');

request.get(process.argv[2])
  .on('response', function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      console.log(`code: ${response.statusCode}`)
    }
  }
);
