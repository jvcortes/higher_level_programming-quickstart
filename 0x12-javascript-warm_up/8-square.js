#!/usr/bin/node
// Prints a first argument-determined size square of 'x' characters. 
const SIZE = parseInt(process.argv[2])
if (SIZE) {
  for (let i = 0; i < SIZE; i++) {
    console.log([...Array(SIZE).fill('X')].join(''));
  }
} else {
  console.log('Missing size');
}
