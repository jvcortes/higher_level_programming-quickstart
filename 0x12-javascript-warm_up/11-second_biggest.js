#!/usr/bin/node
// Prints the second biggest integer in its arguments.
if (process.argv.length > 3) {
  const sorted = process.argv.slice(2).map((val, index) => parseInt(val)).sort();
  console.log(sorted[sorted.length - 2]);
} else {
  console.log(0);
}
