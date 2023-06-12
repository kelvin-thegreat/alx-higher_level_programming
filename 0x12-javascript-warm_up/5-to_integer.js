#!/usr/bin/node

// Script that prints My number: <first argument converted in integer
// If the argument can’t be converted to an integer, print “Not a number”

const parsedInt = parseInt(process.argv[2]);
console.log(Number.isInteger(parsedInt) ? `My number: ${parsedInt}` : "Not a number");

