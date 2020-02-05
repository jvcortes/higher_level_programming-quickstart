#!/usr/bin/node
// Defines a function that will execute n times a function.
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}
