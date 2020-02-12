#!/usr/bin/node
// Makes a HTTP GET request to swapi.co/api/films/:id
const request = require('request');

request(`http://www.swapi.co/api/films/${process.argv[2]}`,
  function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).title);
    }
  }
);
