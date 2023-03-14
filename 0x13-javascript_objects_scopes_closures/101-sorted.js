#!/usr/bin/node
const { dict } = require('./101-data.js');

const userOccurrences = {};
for (const userId in dict) {
  const occurrences = dict[userId];
  if (userOccurrences[occurrences]) {
    userOccurrences[occurrences].push(userId);
  } else {
    userOccurrences[occurrences] = [userId];
  }
}

console.log(userOccurrences);
