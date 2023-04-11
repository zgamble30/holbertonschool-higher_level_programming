#!/usr/bin/node
// Prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer
const num = parseInt(process.argv.slice(2)[0]);
if (!num) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
