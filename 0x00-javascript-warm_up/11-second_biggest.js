#!/usr/bin/node
// Searches the second biggest integer in the list of arguments.
const arg = process.argv;
function compareNumbers (firstValue, secondValue) {
  return firstValue - secondValue;
}
if (arg.length === 2 || arg.length === 3) {
  console.log('0');
} else {
  const argOne = process.argv.slice(2);
  const numbers = [];
  for (let i = 0; i < argOne.length; i++) {
    numbers[i] = parseInt(argOne[i]);
  }
  const nums = numbers.sort(compareNumbers);
  const len = nums.length;
  console.log(nums[len - 2]);
}
