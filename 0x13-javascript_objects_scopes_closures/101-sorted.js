#!/usr/bin/node
// Generates a dictionary of occurrences.
const dict = require('./101-data').dict;

const ret = {};
for (const key in dict) {
  if (!ret[dict[key]]) {
    ret[dict[key]] = [];
  }
  ret[dict[key]].push(key);
}

console.log(ret);
