#!/usr/bin/node

// script that prints a message depending of the number of arguments passed
// If no arguments are passed to the script, print “No argument" else "Argument found”
// one argument is passed to the script, print “Argument found”

const countArgs = process.argv.length;
console.log(countArgs === 2 ? 'No argument' : countArgs === 3 ? 'Argument found' : 'Arguments found');
