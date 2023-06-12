#!/usr/bin/node

//  script that searches the second biggest integer in the list of arguments
//  assume all arguments can be converted to integer

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => b - a);
  console.log(sortedArgs[1]);
}

