#!/usr/bin/node

const num = Number(process.argv[2]);
const str = 'X';

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let output = '';
    for (let n = 0; n < num; n++) {
      output += str;
    }
    console.log(output);
  }
}
