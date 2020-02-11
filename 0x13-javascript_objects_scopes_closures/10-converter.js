#!/usr/bin/node
// Converts a number 
exports.converter = function (base) {
  return (n) => n.toString(base);
}
