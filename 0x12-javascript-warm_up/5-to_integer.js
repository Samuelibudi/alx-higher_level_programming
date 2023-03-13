#!/usr/bin/node

const args = process.argv;
const numberArg = args[2];
const number = parseInt(numberArg);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: %d', number);
}
