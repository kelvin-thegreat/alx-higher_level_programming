#!/usr/bin/node

// script that computes and prints a factorial
// The first argument is integer used for computing the factorial
// Factorial of NaN is 1
// do it recursively, use a function

function factorial(n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

const arg = parseInt(process.argv[2]);

console.log(factorial(arg));

