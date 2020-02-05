#!/usr/bin/node
// Prints the second biggest integer in its arguments.
const sorted = process.argv.slice(2).map((val, index) => parseInt(val)).sort()
console.log(sorted.length > 1 ? sorted[sorted.length - 2] : sorted[0])
