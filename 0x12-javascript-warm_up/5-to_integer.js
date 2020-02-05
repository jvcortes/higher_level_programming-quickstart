#!/usr/bin/node
// Prints "My number: <first argument>"
console.log(
  parseInt(process.argv[2]) ? 'My number: ' + parseInt(
    process.argv[2]) : 'Not a number');
