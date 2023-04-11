#!/usr/bin/node
// Prints the addition of 2 integers
const argOne = parseInt(process.argv.slice(2, 3)[0]);
const argTwo = parseInt(process.argv.slice(3)[0]);
function add (firstValue, secondValue) {
  if (firstValue && secondValue) {
    return (firstValue + secondValue);
  } else {
    return ('NaN');
  }
}
console.log(add(argOne, argTwo));
