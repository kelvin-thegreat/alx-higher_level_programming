#!/usr/bin/node

const x = Math.floor(Number(process.argv[2]));

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  Array(x).fill('C is fun').forEach(line => console.log(line));
}

