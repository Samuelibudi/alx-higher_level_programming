#!/usr/bin/node
const { dict } = require('./101-data').dict;
const nDict = {};

for (const [nDict, occurences] of Object.entries(dict)) {
  if (!nDict[occurences]) {
    nDict[occurences] = [];
  }
  nDict[occurences].push(nDict);
}

console.log(nDict);
