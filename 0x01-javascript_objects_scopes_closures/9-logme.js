#!/usr/bin/node
// function that prints the number of arguments
// already printed and the new argument value
let count = 0;
exports.logMe = function (item) {
  console.log('%d: %s', count, item);
  count = count + 1;
};
