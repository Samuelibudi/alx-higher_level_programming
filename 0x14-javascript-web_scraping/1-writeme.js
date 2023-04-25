#!/usr/bin/node
const fs = require('fs');
const { promisify } = require('util');

const writeFile = promisify(fs.writeFile);

const filePath = process.argv[2];
const content = process.argv[3];

async function writeToFile () {
  try {
    await writeFile(filePath, content, 'utf-8');
  } catch (err) {
    console.error(err);
  }
}

writeToFile();
