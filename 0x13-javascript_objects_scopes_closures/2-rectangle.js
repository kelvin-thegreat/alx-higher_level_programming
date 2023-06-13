#!/usr/bin/node

//  class Rectangle that defines a rectangle
//  use the class notation for defining your class

module.exports = class Rectangle {
  // The constructor must take 2 arguments w and h
  // Initialize the instance attribute width with the value of w
  // Initialize the instance attribute height with the value of h
  constructor (w, h) {
    if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
    }
  }
};
