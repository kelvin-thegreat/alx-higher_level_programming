#!/usr/bin/node

// Update this script by adding a new function incr

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
