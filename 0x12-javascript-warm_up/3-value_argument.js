#!/usr/bin/node
// script that prints the first argument passed to it
// If no arguments are passed to the script, print “No argument”
// use console.log(...) to print all output
// No use of var and length

const args = process.argv[2];

const message = typeof args === "undefined" ? "No argument" : args;

console.log(message);

