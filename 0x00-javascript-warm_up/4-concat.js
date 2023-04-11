#!/usr/bin/node
// Prints two arguments passed to it, in the following format: “ is ”
const argOne = process.argv.slice(2, 3);
const argTwo = process.argv.slice(3);
if (argOne[0] && argTwo[0]) {
  console.log(argOne[0] + ' is ' + argTwo[0]);
} else {
  console.log(argOne[0] + ' is undefined');
}
