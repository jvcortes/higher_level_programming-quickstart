#!/usr/bin/node
// Makes a HTTP GET request to swapi.co/api/people/18
const request = require('request');

request('http://www.swapi.co/api/people/18',
  function (err, response, body) {
    if (err) {
      console.error(err);
    } else {
      console.log(JSON.parse(body).films.length);
    }
  }
);
