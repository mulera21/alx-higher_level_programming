#!/usr/bin/node
// Write a script that prints a message depending of the number of arguments passed:
const num = process.argv.length - 2;

if (num === 0){
    console.log("No argument");
}else if (num === 1) {
    console.log("Argument found");
  } else {
    console.log("Arguments found");
  }
