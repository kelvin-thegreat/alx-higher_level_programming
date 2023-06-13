#!/usr/bin/node

//  script that imports a dictionary of occurrences by user id

const data = require('./101-data').dict;

const result = {};

for (const userId in data) {
  const occurrence = data[userId];

  if (!result[occurrence]) {
    result[occurrence] = [];
  }

  result[occurrence].push(userId);
}

console.log(result);

