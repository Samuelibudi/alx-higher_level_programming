#!/usr/bin/node

const num1 = Number(process.argv[2]);

function fact (a) {
  if (a === 1 || a === 0 || isNaN(a)) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}

console.log(fact(num1));
