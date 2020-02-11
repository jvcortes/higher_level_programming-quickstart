#!/usr/bin/node
// Prints its the number of past arguments plus one and its current argument.
exports.logMe = function fn (item) {
  if (typeof fn.i === 'undefined') {
    fn.i = 0;
  }

  console.log(`${fn.i++}: ${item}`);
};
