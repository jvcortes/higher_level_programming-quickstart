#!/usr/bin/node
// Defines a function that calls a function and increments a number.
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
}
