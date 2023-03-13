#!/usr/bin/node

const myStrings = 'C is fun';

for (let i = 0; i < Number(process.argv[2]); i++) {
  console.log(myStrings);
}
