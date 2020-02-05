#!/usr/bin/node
// Adds two numbers defined by its first two arguments and prints the result.
function add (a, b) {
  return a + b;
}
console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
