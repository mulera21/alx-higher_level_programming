#!/usr/bin/node

function addMeMaybe(number, theFunction) {
    number++; // Increment the number
    theFunction(number); // Call the provided function with the incremented number
  }
  
  module.exports = {
    addMeMaybe: addMeMaybe
  };
  