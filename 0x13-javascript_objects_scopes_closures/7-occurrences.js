#!/usr/bin/node

// function that returns the number of occurrences

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, current) => current === searchElement ? count + 1 : count, 0);
};
