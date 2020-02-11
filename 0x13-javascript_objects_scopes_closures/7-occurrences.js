#!/usr/bin/node
// Returns the number of occurrences of an object in a list.
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  list.forEach((item) => item == searchElement && (i++));
  return i;
}
