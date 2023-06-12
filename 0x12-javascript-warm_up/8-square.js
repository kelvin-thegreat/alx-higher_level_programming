#!/usr/bin/node

// script that prints a square

const size = Math.floor(Number(process.argv[2]));
const errorMessage = isNaN(size) ? 'Missing size' : size > 0 ? Array(size).fill('X'.repeat(size)).join('\n') : '';
console.log(errorMessage);
