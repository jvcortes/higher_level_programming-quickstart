#!/usr/bin/node
// Returns a reversed list
exports.esrever = function (list) {
  reversed  = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }

  return reversed;
}

