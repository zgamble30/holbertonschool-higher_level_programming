#!/usr/bin/node
// Prints x times “C is fun”
const num = parseInt(process.argv.slice(2)[0]);
if (!num) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
