#!/usr/bin/node
// Prints a square
const num = parseInt(process.argv.slice(2)[0]);
const letter = 'X';
if (!num) {
  console.log('Missing size');
} else {
  for (let j = 0; j < num; j++) {
    console.log(letter.repeat(num));
  }
}
