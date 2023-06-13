#!/usr/bin/node

// class Rectangle that defines a rectangle
// use the class notation for defining your class

module.exports = class Rectangle {
  
  // constructor must take 2 arguments: w and h
  // Initialize the instance attribute width with the value of w
  // Initialize the instance attribute height with the value of h

  constructor (w, h) {
     // If w or h is equal to 0 or not a positive integer, create an empty objec
    if (w > 0 && h > 0) { 
	    [this.width, this.height] = [w, h]; 
    }
  }
     // Create an instance method called print()
     // prints the rectangle using the character X 
  print () {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }
};
