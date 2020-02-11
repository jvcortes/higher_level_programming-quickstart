#!/usr/bin/node
// Computes a new array from another array.
const list = require('./100-data').list;

console.log(list);
console.log(list.map((val, index) => val * index));
