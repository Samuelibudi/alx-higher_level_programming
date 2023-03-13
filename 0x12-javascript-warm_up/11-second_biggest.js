#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const args = process.argv.slice(2);
  const numbers = args.map(Number);
  const sortedNumbers = numbers.sort((a, b) => b - a);
  console.log(sortedNumbers[1]);
}
