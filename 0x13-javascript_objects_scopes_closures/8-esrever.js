#!/usr/bin/node

// function that returns the reversed version of a list

exports.esrever = function (list) {
  return list.reduceRight((reversed, current) => {
    reversed.push(current);
    return reversed;
  }, []);
};

