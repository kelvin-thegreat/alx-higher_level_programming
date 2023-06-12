#!/usr/bin/node

// script that prints a square

const sqrSize = Math.floor(Number(process.argv[2]));
if (isNaN(sqrSize)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < sqrSize; r++) {
    let row = '';
    for (let c = 0; c < sqrSize; c++) row += 'X';
    console.log(row);
  }
}
