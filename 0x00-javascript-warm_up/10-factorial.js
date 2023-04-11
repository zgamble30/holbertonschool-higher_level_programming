#!/usr/bin/node
// Computes and prints a factorial
const num = parseInt(process.argv.slice(2, 3)[0]);
function factorial (value) {
  if (!value) {
    return ('1');
  } else {
    return value * factorial(value - 1);
  }
}
console.log(factorial(num));
